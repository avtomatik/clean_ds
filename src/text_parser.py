#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:28:58 2023

@author: green-machine
"""


import io
from pathlib import Path

from pandas import DataFrame

PATH_SRC = '/home/green-machine/Downloads'
FILE_NAME = 'books_plus.txt'

DICT_KEYS = [
    'Автор', 'Название', 'Цена', 'Издательство', 'ISBN', 'Год издания', 'Тираж', 'Количество страниц', 'Обложка', 'Формат'
]

filepath = Path(PATH_SRC).joinpath(FILE_NAME)
with io.open(filepath, encoding='utf-8') as text_file:

    entries, block = [], []

    for line in text_file.read().splitlines():
        if not line:
            block = []
            if not block:
                entries.append(block)
            continue
        block.append(line)


books = []

for entry in filter(bool, entries):
    if any(filter(lambda _: '\t' in _, entry)):
        cols_dict = dict(filter(lambda _: '\t' in _[1], enumerate(entry)))
        vals_dict = dict(filter(lambda _: not '\t' in _[1], enumerate(entry)))

        if all(map(lambda _: _[0] - _[-1] == 1, zip(vals_dict, cols_dict))):
            book_dict = dict(
                zip(
                    map(lambda _: _.replace(':\t', ''), cols_dict.values()),
                    vals_dict.values()
                )
            )
    else:
        # =====================================================================
        # To Parse the Rest of Lines According To DICT_KEYS
        # =====================================================================
        book_dict = dict(zip(DICT_KEYS, entry))

    books.append(book_dict)


FILE_NAME = 'books.xlsx'
df = DataFrame.from_dict(books)
df['Цена'] = df['Цена'].str.split().str.get(0).astype(int)
excel_writer = Path(PATH_SRC).joinpath(FILE_NAME)
kwargs = {
    'excel_writer': excel_writer,
    'index': False
}
df.to_excel(**kwargs)
