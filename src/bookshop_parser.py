#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:28:58 2023

@author: green-machine
"""


from book_processor import BookNormalizer, BookReader, BookWriter, PriceParser
from config import PATH

FILE_NAME_SRC = 'books_plus.txt'
FILE_NAME_DST = 'books_plus.csv'


def main():
    input_path = PATH / FILE_NAME_SRC
    output_path = PATH / FILE_NAME_DST

    reader = BookReader(input_path)
    raw_books = reader.read_books()

    normalizer = BookNormalizer(PriceParser())
    normalized_books = [normalizer.normalize(book) for book in raw_books]

    writer = BookWriter(output_path)
    writer.write(normalized_books)

    print(f'Successfully saved {len(normalized_books)} books to {output_path}')


if __name__ == '__main__':
    main()
