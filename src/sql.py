import json
import sqlite3

import pandas as pd
import pandas.io.sql as sql
import psycopg2
import pymongo
import requests


def get_psql_cursor():
    conn = psycopg2.connect(
        dbname='stickers',
        user='stickers_admin',
        password='qwerty',
        host='localhost'
    )
    # =========================================================================
    # Return Cursor
    # =========================================================================
    return conn.cursor()


def get_sqlite3_cursor():
    query = """
    CREATE TABLE test
    (
      a VARCHAR(20),
      b VARCHAR(20),
      c REAL,
      d INTEGER
    )
    ;
"""
    conn = sqlite3.connect(':memory:')
    conn.execute(query)
    conn.commit()

    data = [
        ('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5),
    ]
    stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
    conn.executemany(stmt, data)
    conn.commit()

    cursor = conn.execute('SELECT * FROM test')
    rows = cursor.fetchall()
    print(sql.read_sql('SELECT * FROM test', conn))


def get_data_frame_mongo():
    conn = pymongo.MongoClient('localhost', 27017)

    tweets = conn.db.tweets

    url = 'http://search.twitter.com/search.json?q=python%20pandas'
    data = json.loads(requests.get(url).text)

    for tweet in data['results']:
        tweets.save(tweet)

    cursor = tweets.find({'from_user': 'wesmckinn'})

    tweet_fields = ['created_at', 'from_user', 'id', 'text']
    result = pd.DataFrame(list(cursor), columns=tweet_fields)
