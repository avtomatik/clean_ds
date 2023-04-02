#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:53:19 2022

@author: Alexander Mikhailov
"""

# =============================================================================
# Depreciation Types
# =============================================================================


from dataclasses import dataclass


@dataclass
class Configuration:
    value: int
    life: int
    rate: float
    initial: int


def print_out(stock):
    for _, value in enumerate(stock):
        print(f'Year {_:2n}: {value:,.2f}')


# =============================================================================
# Linear Depreciation
# =============================================================================
value = 1000000
life = 50
rate = 1

stock = [value, ]
for year in range(life):
    delta = value * rate / life
    stock.append(stock[year] - delta)

print_out(stock=stock)

# =============================================================================
# Geomertic Depreciation
# =============================================================================
value = 1000000
life = 50
rate = 2

stock = [value, ]
for year in range(life):
    delta = value * rate / life * (1 - rate / life) ** (year - 1)
    stock.append(stock[year] - delta)

print_out(stock=stock)

# =============================================================================
# Hyperbolic Depreciation
# =============================================================================
value = 1000000
life = 50
rate = 0.1

stock = [value, ]
for year in range(life):
    delta = value * ((life - (year - 1)) / (life - rate * (year - 1)) -
                     (life - year) / (life - rate * year))
    stock.append(stock[year] - delta)

print_out(stock=stock)

# =============================================================================
# Ивашкевич В. Б. Бухгалтерский управленческий учет, Page 145, Depreciation
# =============================================================================
value = 70000
life = 7
initial = 16000

stock = [value, ]
for year in range(life):
    delta = 2 * (0 - value + initial * life) / (life * (life - 1))
    stock.append(stock[year] - delta)

print_out(stock=stock)
