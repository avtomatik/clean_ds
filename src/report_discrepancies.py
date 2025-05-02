#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:37:49 2022

@author: green-machine
"""

import zipfile
from itertools import combinations

import pandas as pd

from config import BASE_PATH, DATA_PATH
from funcs import transliterate, trim_columns

ARCHIVE_NAME = 'cherkizovo.zip'
FILE_NAME = 'cherkizovo.xlsx'

# =============================================================================
# Step 1
# =============================================================================
csv_paths = []

# Process Excel files and collect CSV paths
for file_path in DATA_PATH.iterdir():
    if not file_path.is_file() or file_path.suffix != '.xlsx':
        continue
    df = pd.read_excel(file_path, skiprows=[1])
    df.columns = map(transliterate, df.columns)
    csv_path = DATA_PATH / f'data_{int(file_path.stem):04n}.csv'
    df.pipe(trim_columns).to_csv(csv_path, index=False)
    csv_paths.append(csv_path)
    file_path.unlink()

# Archive all generated CSVs
with zipfile.ZipFile(DATA_PATH / ARCHIVE_NAME, 'w') as archive:
    for csv_path in csv_paths:
        archive.write(
            csv_path,
            arcname=csv_path.name,
            compress_type=zipfile.ZIP_DEFLATED
        )
        csv_path.unlink()


# =============================================================================
# Step 2
# =============================================================================
df_total = pd.DataFrame()

data_chunks = []

with zipfile.ZipFile(DATA_PATH / ARCHIVE_NAME, 'w') as archive:
    for file in archive.filelist:
        with archive.open(file.filename) as f:
            df = pd.read_csv(f)
            df['source'] = file.filename
            data_chunks.append(df)


df_total = pd.concat(data_chunks, ignore_index=True)

df_total = df_total[
    [col for col in df_total.columns if col != 'source'] + ['source']
]

df_total.to_excel(DATA_PATH / FILE_NAME, index=False)

#

df = pd.read_excel(DATA_PATH / FILE_NAME)

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
