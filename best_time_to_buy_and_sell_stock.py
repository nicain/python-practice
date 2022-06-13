"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


leetcode_url = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock'

card_url = 'https://www.brainscape.com/decks/11570817/cards/387298224/edit'


def answer(nums):
  
  lwm = float('inf')
  diff = 0
  for x in nums:
    if x < lwm:
      lwm = x
    else:
      diff = max(diff, x-lwm)
  return diff
