#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:41:59 2022

@author: Alexander Mikhailov
"""


import pandas as pd

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def count_score(hand: list[int]) -> int:
    cadet_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    hand_aces = [card for card in hand if not card in cadet_cards]

    score = sum(cadet_cards[card] for card in hand if card in cadet_cards)
    for card in hand_aces:
        if score <= 10:
            score += 11
        else:
            score += 1
    return score


def blackjack_hand_greater_than(hand_1: list[str], hand_2: list[str]) -> bool:
    """ Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a series_id.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    score_hand_1 = count_score(hand_1)
    score_hand_2 = count_score(hand_2)
    if score_hand_1 <= 21:
        if score_hand_2 <= 21:
            return score_hand_1 > score_hand_2
        else:
            return True
    else:
        return False


# def main():
#     hand_1 = ['2', '10', '5', 'A', '9', '9']
#     hand_2 = ['5', '7', '5', 'Q', '5']
#     print(blackjack_hand_greater_than(hand_1, hand_2))


# if __name__ == '__main__':
#     main()


iowa_file_path = "~/github/bmstu/data/external/iowa_train.csv"

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
features = [
    "LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"
]
X = home_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print(f"Validation MAE: {val_mae:,.0f}")


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(
        max_leaf_nodes=max_leaf_nodes, random_state=0
    )
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
maes = {
    get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y): max_leaf_nodes
    for max_leaf_nodes in candidate_max_leaf_nodes
}

# =============================================================================
# best_tree_size = min(maes, key=maes.get)
# =============================================================================
