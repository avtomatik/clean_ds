#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:37:49 2022

@author: green-machine
"""

import os
import zipfile
from itertools import combinations
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from pandas import DataFrame

from config import PATH

ARCHIVE_NAME = 'cherkizovo.zip'
FILE_NAME = 'cherkizovo.xlsx'
# =============================================================================
# Step 1
# =============================================================================

# =============================================================================
# for file_name in tuple(os.listdir(BASE_DIR)):
#     df = pd.read_excel(PATH.joinpath(file_name), skiprows=[1])
#     df.columns = map(transliterate, df.columns)
#     df.pipe(trim_columns).to_csv(
#         PATH.joinpath(
#             f'data_{int(Path(file_name).stem):04n}.csv'),
#         index=False
#     )
#     os.unlink(PATH.joinpath(file_name))
# =============================================================================

# =============================================================================
# file_names = tuple(os.listdir(BASE_DIR))
# with ZipFile(PATH.joinpath(ARCHIVE_NAME), 'w') as archive:
#     for file_name in file_names:
#         archive.write(PATH.joinpath(file_name), compress_type=zipfile.ZIP_DEFLATED)
#         os.unlink(PATH.joinpath(file_name))
# =============================================================================

# =============================================================================
# Step 2
# =============================================================================
# =============================================================================
# total = DataFrame()
# with ZipFile(PATH.joinpath(ARCHIVE_NAME), 'w') as archive:
#     for item in archive.filelist:
#         with archive.open(item.filename) as f:
#             chunk = pd.read_csv(f)
#             chunk['source'] = item.filename
#             total = pd.concat([total, chunk])
# =============================================================================

# columns = list(total.columns)
# columns.remove('source')
# total = total.reindex(columns=columns + ['source'])
# total.to_excel(PATH.joinpath(FILE_NAME), index=False)

df = pd.read_excel(PATH.joinpath(FILE_NAME))
plan_breakdown = {}
for _ in range(df.shape[0]):
    if df.iloc[_, -1] == 'Y':
        plan = df.iloc[_, -4]
        detailed = df.iloc[_, -3]
        plan_breakdown.setdefault(plan, {})
        plan_breakdown[plan].setdefault(detailed, set())
        plan_breakdown[plan][detailed].add(df.iloc[_, -2])

FILE_NAME = 'cherkizovo_diff_report.txt'
with open(PATH.joinpath(FILE_NAME), 'w') as f:
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
