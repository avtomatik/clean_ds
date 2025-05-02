#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:37:49 2022

@author: green-machine
"""

import io
import zipfile
from abc import ABC, abstractmethod
from itertools import combinations
from pathlib import Path

import pandas as pd

from config import BASE_PATH, DATA_PATH
from funcs import transliterate, trim_columns

ARCHIVE_NAME = 'cherkizovo.zip'
TEXT_REPORT_NAME = 'cherkizovo_diff_report.txt'


class FileHandler(ABC):
    """Abstract class for file handling (DIP)."""

    @abstractmethod
    def read_file(self, file_path: Path):
        pass

    @abstractmethod
    def process_file(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def save_to_buffer(self, df: pd.DataFrame) -> io.StringIO:
        pass


class ExcelFileHandler(FileHandler):
    """Concrete implementation for handling Excel files (SRP)."""

    def read_file(self, file_path: Path) -> pd.DataFrame:
        return pd.read_excel(file_path, skiprows=[1])

    def process_file(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = map(transliterate, df.columns)
        return trim_columns(df)

    def save_to_buffer(self, df: pd.DataFrame) -> io.StringIO:
        buffer = io.StringIO()
        df.to_csv(buffer, index=False)
        return buffer


class ArchiveHandler(ABC):
    """Abstract class for archive handling (DIP)."""

    @abstractmethod
    def write_to_archive(
        self,
        archive: zipfile.ZipFile,
        file_name: str,
        content: io.StringIO
    ):
        pass

    @abstractmethod
    def read_from_archive(self, archive: zipfile.ZipFile) -> pd.DataFrame:
        pass


class ZipArchiveHandler(ArchiveHandler):
    """Concrete implementation for ZIP archive handling (SRP)."""

    def write_to_archive(
        self,
        archive: zipfile.ZipFile,
        file_name: str,
        content: io.StringIO
    ):
        archive.writestr(file_name, content.getvalue())

    def read_from_archive(self, archive: zipfile.ZipFile) -> pd.DataFrame:
        data_chunks = []
        for file in archive.filelist:
            with archive.open(file.filename) as f:
                chunk = pd.read_csv(f)
                chunk['source'] = file.filename
                data_chunks.append(chunk)
        return pd.concat(data_chunks, ignore_index=True)


class ReportGenerator:
    """Responsible for generating the final report (SRP)."""

    def generate(self, plan_breakdown: dict, output_path: Path):
        with output_path.open('w', encoding='utf-8') as f:
            for plan, detailed_map in plan_breakdown.items():
                print('#' * 100, file=f)
                print(f'{plan:^100}', file=f)
                print('#' * 100, file=f)
                print(file=f)

                for one, another in combinations(detailed_map.keys(), 2):
                    print('#' * 50, file=f)
                    print(
                        f'Сравнение <{plan} {one}> с <{plan} {another}>:',
                        file=f
                    )
                    print('#' * 50, file=f)

                    left_diff = sorted(
                        detailed_map[one] - detailed_map[another])
                    right_diff = sorted(
                        detailed_map[another] - detailed_map[one])

                    if left_diff:
                        print(f'- Отмечено в <{plan} {one}>, отсутствует в '
                              f'<{plan} {another}>:', file=f)
                        for lpu in left_diff:
                            print(f'-- {lpu}', file=f)
                    if right_diff:
                        print(f'- Отмечено в <{plan} {another}>, отсутствует в '
                              f'<{plan} {one}>:', file=f)
                        for lpu in right_diff:
                            print(f'-- {lpu}', file=f)

                    if not left_diff and not right_diff:
                        print('- Нет отличий.', file=f)

                    print(file=f)


class DataProcessor:
    """Coordinates all operations (SRP)."""

    def __init__(
        self,
        file_handler: FileHandler,
        archive_handler: ArchiveHandler, report_generator: ReportGenerator
    ):
        self.file_handler = file_handler
        self.archive_handler = archive_handler
        self.report_generator = report_generator

    def process_files(
        self,
        data_path: Path,
        archive_path: Path,
        report_path: Path
    ):
        """Main workflow for processing files, creating archive, and generating report."""
        data_chunks = []
        with zipfile.ZipFile(archive_path, 'w') as archive:
            for file_path in data_path.iterdir():
                if not file_path.is_file() or file_path.suffix != '.xlsx':
                    continue

                chunk = self.file_handler.read_file(file_path)
                chunk_clean = self.file_handler.process_file(chunk)

                # Write to archive
                csv_buffer = self.file_handler.save_to_buffer(chunk_clean)
                csv_name = f'data_{int(file_path.stem):04n}.csv'
                self.archive_handler.write_to_archive(
                    archive, csv_name, csv_buffer)

                # Add to data collection
                chunk_clean['source'] = csv_name
                data_chunks.append(chunk_clean)

                file_path.unlink()

        df = pd.concat(data_chunks, ignore_index=True)
        df = df[[col for col in df.columns if col != 'source'] + ['source']]

        # Generate the report
        plan_breakdown = self.generate_plan_breakdown(df)
        self.report_generator.generate(plan_breakdown, report_path)

    def generate_plan_breakdown(self, df: pd.DataFrame) -> dict:
        """Generates a breakdown of the plans and their differences."""
        plan_breakdown = {}
        for _, row in df.iterrows():
            if row.iloc[-1] == 'Y':
                plan = row.iloc[-4]
                detailed = row.iloc[-3]
                value = row.iloc[-2]
                plan_breakdown.setdefault(plan, {}).setdefault(
                    detailed, set()).add(value)
        return plan_breakdown


def main():
    file_handler = ExcelFileHandler()
    archive_handler = ZipArchiveHandler()
    report_generator = ReportGenerator()

    processor = DataProcessor(file_handler, archive_handler, report_generator)
    archive_path = DATA_PATH / ARCHIVE_NAME
    text_report_path = BASE_PATH / TEXT_REPORT_NAME
    processor.process_files(DATA_PATH, archive_path, text_report_path)


if __name__ == '__main__':
    main()
