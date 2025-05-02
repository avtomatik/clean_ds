#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:49:26 2022

@author: alexandermikhailov
"""

import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# =============================================================================
# Brett Vanderblock
# =============================================================================
df_iris = load_iris()
columns = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

df_iris = pd.concat(
    [
        pd.DataFrame(data=df_iris.data, columns=columns),
        pd.DataFrame(data=df_iris.target, columns=['species'])
    ],
    axis=1
)


# =============================================================================
# # =============================================================================
# # Boxplot
# # =============================================================================
# df_iris.boxplot()
# =============================================================================


# =============================================================================
# Correlation Matrix
# =============================================================================
# =============================================================================
# Another Implementation
# =============================================================================
df_iris.corr().style.background_gradient(cmap='RdYlGn', axis=None)
sns.heatmap(df_iris.corr(), annot=True)


COLORS = {
    'versicolor': 'red',
    'setosa': 'green',
    'virginica': 'blue',
}

df_iris['colors'] = df_iris['species'].map(COLORS)
df_iris.plot.scatter(
    x='sepal_width',
    y='sepal_length',
    color=df_iris['colors']
)
