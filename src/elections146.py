# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:23:22 2021

@author: Alexander Mikhailov
"""

from pandas import DataFrame


def main():
    data = {
        'Единая Россия': 58.99,
        'КПРФ': 32.96,
        'ЛДПР': 23.74,
        'Справедливая Россия': 19.41,
        'Яблоко': 9.32,
        'Партиоты России': 1.46,
        'Правое дело': 0.59
    }
    df = DataFrame(
        zip(data.keys(), data.values()),
        columns=['parties', 'percentages']
    )
    df['corrected'] = df.iloc[:, 1].div(df.iloc[:, 1].sum())
    return df


if __name__ == '__main__':
    main()
