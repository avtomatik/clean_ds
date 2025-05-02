#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 11:37:58 2025

@author: alexandermikhailov
"""


import csv
import re
from pathlib import Path
from typing import Dict, List, Union

DICT_KEYS = [
    'Автор',
    'Название',
    'Цена',
    'Издательство',
    'ISBN',
    'Год издания',
    'Тираж',
    'Количество страниц',
    'Обложка',
    'Формат',
]


class BookReader:
    """Reads raw book data from a text file."""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read_books(self) -> List[List[str]]:
        books = []
        current_book = []

        with self.file_path.open(encoding='utf-8') as f:
            for line in list(f) + ['\n']:  # Sentinel line
                stripped = line.strip()
                if stripped:
                    current_book.append(stripped)
                elif current_book:
                    books.append(current_book)
                    current_book = []

        return books


class PriceParser:
    """Extracts numeric value from price strings."""

    @staticmethod
    def extract(price_str: str) -> Union[int, None]:
        match = re.search(r'\d+', price_str)
        return int(match.group()) if match else None


class BookNormalizer:
    """Normalizes raw book entries to dicts with consistent keys."""

    def __init__(self, price_parser: PriceParser):
        self.price_parser = price_parser

    def normalize(self, entry: List[str]) -> Dict[str, Union[str, int, None]]:
        book = {key: '' for key in DICT_KEYS}

        if any(item.endswith(':') for item in entry):
            # Format B: alternating label/value
            for i in range(0, len(entry) - 1, 2):
                key = entry[i].rstrip(':').strip()
                value = entry[i + 1].strip()
                if key in book:
                    book[key] = value
        else:
            # Format A: positional + prefixed values
            book['Автор'] = entry[0]
            book['Название'] = entry[1]
            book['Цена'] = entry[2]

            for item in entry[3:]:
                for key in DICT_KEYS[3:]:
                    if item.startswith(
                        (f'{key}:', f'{key} (', f'{key} (мм):')
                    ):
                        book[key] = item.split(':', 1)[-1].strip()
                    elif key == (
                        'Количество страниц' and item.startswith('Страниц:')
                    ):
                        book[key] = item.split(':', 1)[-1].strip()

        # Normalize price
        book['Цена'] = self.price_parser.extract(book['Цена'])

        return book


class BookWriter:
    """Writes normalized book data to CSV."""

    def __init__(self, output_path: Path):
        self.output_path = output_path

    def write(self, books: List[Dict[str, Union[str, int]]]) -> None:
        with self.output_path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=DICT_KEYS)
            writer.writeheader()
            writer.writerows(books)
