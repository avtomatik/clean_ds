#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:28:58 2023

@author: green-machine
"""


from book_processor import BookNormalizer, BookReader, BookWriter, PriceParser
from config import BASE_PATH

FILE_NAME_SRC = 'books_plus.txt'
FILE_NAME_DST = 'books_plus.csv'


def main():
    file_path_src = BASE_PATH / FILE_NAME_SRC
    file_path_dst = BASE_PATH / FILE_NAME_DST

    reader = BookReader(file_path_src)
    raw_books = reader.read_books()

    normalizer = BookNormalizer(PriceParser())
    normalized_books = [normalizer.normalize(book) for book in raw_books]

    writer = BookWriter(file_path_dst)
    writer.write(normalized_books)

    print(
        f'Successfully saved {len(normalized_books)} books to {file_path_dst}'
    )


if __name__ == '__main__':
    main()
