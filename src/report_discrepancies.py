#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:37:49 2022

@author: green-machine
"""

import io
import zipfile
from itertools import combinations

import pandas as pd

from config import BASE_PATH, DATA_PATH
from funcs import transliterate, trim_columns

ARCHIVE_NAME = 'cherkizovo.zip'
FILE_NAME = 'cherkizovo.xlsx'


archive_path = DATA_PATH / ARCHIVE_NAME

# Step 1 & 2: Process .xlsx files, archive to ZIP in-memory, and collect DataFrames
data_chunks = []
with zipfile.ZipFile(archive_path, 'w') as archive:
    for file_path in DATA_PATH.iterdir():
        if not file_path.is_file() or file_path.suffix != '.xlsx':
            continue

        chunk = pd.read_excel(file_path, skiprows=[1])
        chunk.columns = map(transliterate, chunk.columns)
        chunk_cleaned = trim_columns(chunk)

        # Write cleaned CSV into archive (in memory)
        csv_buffer = io.StringIO()
        chunk_cleaned.to_csv(csv_buffer, index=False)
        csv_name = f'data_{int(file_path.stem):04n}.csv'
        archive.writestr(csv_name, csv_buffer.getvalue())

        # Add to in-memory collection
        chunk_cleaned['source'] = csv_name
        data_chunks.append(chunk_cleaned)

        file_path.unlink()

# Step 3: Combine all into one final DataFrame
df = pd.concat(data_chunks, ignore_index=True)
df = df[[col for col in df.columns if col != 'source'] + ['source']]

plan_breakdown = {}

for _ in range(df.shape[0]):
    if df.iloc[_, -1] == 'Y':
        plan = df.iloc[_, -4]
        detailed = df.iloc[_, -3]
        plan_breakdown.setdefault(plan, {})
        plan_breakdown[plan].setdefault(detailed, set())
        plan_breakdown[plan][detailed].add(df.iloc[_, -2])

FILE_NAME = 'cherkizovo_diff_report.txt'

with (BASE_PATH / FILE_NAME).open('w') as f:
    for plan, value in plan_breakdown.items():
        print('#' * 100, file=f)
        print(f'{plan:^100}', file=f)
        print('#' * 100, file=f)
        print(file=f)
        for one, another in combinations(value.keys(), 2):
            print('#' * 50, file=f)
            print(f'Сравнение <{plan} {one}> с <{plan} {another}>:', file=f)
            print('#' * 50, file=f)
            left_diff = sorted(value[one] - value[another])
            right_diff = sorted(value[another] - value[one])
            if left_diff:
                print(
                    f'- Отмечено в <{plan} {one}>, отсутствует в <{plan} {another}>:',
                    file=f
                )
                for lpu in sorted(left_diff):
                    print(f'-- {lpu}', file=f)
            elif right_diff:
                print(
                    f'- Отмечено в <{plan} {another}>, отсутствует в <{plan} {one}>:',
                    file=f
                )
                for lpu in sorted(right_diff):
                    print(f'-- {lpu}', file=f)
            else:
                print('- Нет отличий.', file=f)
            print(file=f)
