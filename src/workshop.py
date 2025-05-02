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
iris = load_iris()
iris = pd.concat(
    [
        pd.DataFrame(
            data=iris.data,
            columns=(
                'sepal length',
                'sepal width',
                'petal length',
                'petal width'
            )
        ),
        pd.DataFrame(data=iris.target, columns=('species',))
    ],
    axis=1
)
# =============================================================================
# Boxplot
# =============================================================================
iris.boxplot()

# =============================================================================
# Correlation Matrix
# =============================================================================
# =============================================================================
# Another Implementation
# =============================================================================
iris.corr().style.background_gradient(cmap='RdYlGn', axis=None)
sns.heatmap(iris.corr(), annot=True)

colors = {
    'versicolor': 'red',
    'setosa': 'green',
    'virginica': 'blue',
}
iris['colors'] = iris['species'].map(colors)
iris.plot.scatter(x='sepal_width', y='sepal_length', color=iris['colors'])
