#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:49:26 2022

@author: alexandermikhailov

Exploratory Data Analysis on the Iris Dataset.

Visualizations:
- Boxplot of features
- Correlation heatmap
- Sepal scatter plot colored by species
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris


def load_iris_dataframe() -> pd.DataFrame:
    """Load and format the Iris dataset as a pandas DataFrame."""
    iris = load_iris()
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    df = pd.DataFrame(iris.data, columns=features)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df


def plot_boxplot(df: pd.DataFrame) -> None:
    """Show a boxplot of all numeric features."""
    df.boxplot()
    plt.title("Boxplot of Iris Features")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Plot a correlation heatmap of the dataset's numeric features."""
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='RdYlGn')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_sepal_scatter(df: pd.DataFrame) -> None:
    """Create a scatter plot of sepal width vs. sepal length."""
    color_map = {'setosa': 'green', 'versicolor': 'red', 'virginica': 'blue'}
    df['color'] = df['species'].map(color_map)
    df.plot.scatter(
        x='sepal_width',
        y='sepal_length',
        color=df['color'],
        title='Sepal Width vs Length by Species'
    )
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def main():
    # =========================================================================
    # Brett Vanderblock
    # =========================================================================
    df_iris = load_iris_dataframe()
    plot_boxplot(df_iris)
    plot_correlation_heatmap(df_iris)
    plot_sepal_scatter(df_iris)


if __name__ == '__main__':
    main()
