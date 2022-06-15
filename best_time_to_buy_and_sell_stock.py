"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


source_url = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock'

card_url = 'https://www.brainscape.com/decks/11570817/cards/387298224/edit'


import typing


def answer(prices: typing.Sequence):
  
  lwm = float('inf')
  diff = 0
  for x in prices:
    if x < lwm:
      lwm = x
    else:
      diff = max(diff, x-lwm)
  return diff


def test_case1():
  prices = [7,1,5,3,6,4]
  expected_result = 5
  assert expected_result == answer(prices)


def test_case2():
  prices = [7,6,4,3,1]
  expected_result = 0
  assert expected_result == answer(prices)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])
