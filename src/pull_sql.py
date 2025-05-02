#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:32:17 2022

@author: Alexander Mikhailov
"""


from fetchers import MongoTweetRetriever, PostgresConnection, SQLiteInMemory


def main():
    # SQLite Example
    sqlite_db = SQLiteInMemory()
    df_sqlite = sqlite_db.fetch_data()
    print('SQLite Data:')
    print(df_sqlite)

    # PostgreSQL Connection Example (cursor only)
    pg_conn = PostgresConnection(
        dbname='stickers',
        user='stickers_admin',
        password='qwerty'
    )
    cursor = pg_conn.get_cursor()
    print('PostgreSQL cursor acquired.')

    # Mongo Example (commented to avoid actual API calls)
    # mongo_retriever = MongoTweetRetriever()
    # df_mongo = mongo_retriever.fetch_data()
    # print('Mongo Data:')
    # print(df_mongo)


if __name__ == '__main__':
    main()
