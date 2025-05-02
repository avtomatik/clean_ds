#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 22:03:34 2025

@author: alexandermikhailov
"""

import json
import sqlite3
from abc import ABC, abstractmethod

import pandas as pd
import pandas.io.sql as sql
import psycopg2
import pymongo
import requests

# ==============================
# Abstract Interfaces (DIP)
# ==============================


class DatabaseConnection(ABC):
    @abstractmethod
    def get_cursor(self):
        pass


class DataRetriever(ABC):
    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        pass


# ==============================
# PostgreSQL Implementation (SRP)
# ==============================

class PostgresConnection(DatabaseConnection):
    def __init__(self, dbname, user, password, host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def get_cursor(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        return conn.cursor()


# ==============================
# SQLite Implementation (SRP)
# ==============================

class SQLiteInMemory(DatabaseConnection, DataRetriever):
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self._init_schema()
        self._insert_sample_data()

    def _init_schema(self):
        query = """
        CREATE TABLE test (
            a VARCHAR(20),
            b VARCHAR(20),
            c REAL,
            d INTEGER
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def _insert_sample_data(self):
        data = [
            ('Atlanta', 'Georgia', 1.25, 6),
            ('Tallahassee', 'Florida', 2.6, 3),
            ('Sacramento', 'California', 1.7, 5),
        ]
        stmt = 'INSERT INTO test VALUES (?, ?, ?, ?)'
        self.conn.executemany(stmt, data)
        self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def fetch_data(self) -> pd.DataFrame:
        return sql.read_sql('SELECT * FROM test;', self.conn)


# ==============================
# MongoDB + API Data Retriever (SRP)
# ==============================

class MongoTweetRetriever(DataRetriever):
    def __init__(self, host='localhost', port=27017):
        self.conn = pymongo.MongoClient(host, port)
        self.db = self.conn.db
        self.tweets = self.db.tweets

    def fetch_data(self) -> pd.DataFrame:
        url = 'http://search.twitter.com/search.json?q=python%20pandas'
        response = requests.get(url)
        data = json.loads(response.text)

        for tweet in data.get('results', []):
            self.tweets.save(tweet)

        cursor = self.tweets.find({'from_user': 'wesmckinn'})
        tweet_fields = ['created_at', 'from_user', 'id', 'text']
        return pd.DataFrame(list(cursor), columns=tweet_fields)
