"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick."""

source_url = 'https://leetcode.com/explore/interview/card/google/67/sql-2/3046/'

card_url = None


def answer(fruits):
  li = 0
  basket = {}
  for ri, curr_fruit in enumerate(fruits):
    basket[curr_fruit] = basket.get(curr_fruit, 0) + 1
    if len(basket) > 2:
      basket[fruits[li]] -= 1
      if basket[fruits[li]] == 0: 
        del basket[fruits[li]]
      li += 1
  return ri - li + 1 


class Solution:
    def totalFruit(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1():
  args = ([1,2,1],)
  expected_result = 3
  assert expected_result == answer(*args)


def test_case2():
  args = ([1,2,3,2,2],)
  expected_result = 4
  assert expected_result == answer(*args)


def test_case3():
  args = ([0,1,2,2],)
  expected_result = 3
  assert expected_result == answer(*args)


def test_case4():
  args = ([3,3,3,1,1],)
  expected_result = 5
  assert expected_result == answer(*args)


def test_case5():
  args = ([1,1,1,1,1,2,2,2,1,1,3,3,3,4,4,4],)
  expected_result = 10
  expected_result == answer(*args)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])
