#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:28:58 2023

@author: green-machine
"""


import pandas as pd

from config import PATH

FILE_NAME = 'books_plus.txt'

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
    'Формат'
]


file_path = PATH.joinpath(FILE_NAME)

with file_path.open(encoding='utf-8') as f:
    books_data, book_data = [], []

    for line in list(f) + ['\n']:
        stripped = line.strip()

        if stripped:
            book_data.append(stripped)
        elif book_data:
            books_data.append(book_data)
            book_data = []


books = []

for book_data in books_data:
    if any('\t' in field for field in book_data):
        cols_dict = {}
        vals_dict = {}

        for index, value in enumerate(book_data):
            if '\t' in value:
                cols_dict[index] = value
            else:
                vals_dict[index] = value

        if all(
            val_idx - col_idx == 1
            for val_idx, col_idx in zip(vals_dict, cols_dict)
        ):
            keys = [val.replace(':\t', '') for val in cols_dict.values()]
            values = list(vals_dict.values())
            book_dict = dict(zip(keys, values))
        else:
            book_dict = {}
    else:
        # =====================================================================
        # To Parse the Rest of Lines According To DICT_KEYS
        # =====================================================================
        book_dict = dict(zip(DICT_KEYS, book_data))

    books.append(book_dict)


df = pd.DataFrame.from_dict(books)
df['Цена'] = df['Цена'].str.split().str.get(0).astype(int)

FILE_NAME = 'books.xlsx'

file_path = PATH.joinpath(FILE_NAME)
df.to_excel(file_path, index=False)
