#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:00:26 2025

@author: alexandermikhailov
"""


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR.joinpath('data')

BOOKS_NAME = 'books.txt'

ARCHIVE_NAME = 'cherkizovo.zip'

TEXT_REPORT_NAME = 'cherkizovo_diff_report.txt'
