"""Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

source_url = 'https://leetcode.com/problems/binary-search/'

card_url = 'https://www.brainscape.com/decks/11570817/cards/387306182/edit'


import typing


def answer(
  nums: typing.Sequence, 
  target: int
) -> int:
  
  li, ri = 0, len(nums)-1
  while li <= ri:
    mi = int((li + ri)/2)
    if nums[mi] == target:
      return mi
    if target < nums[mi]:
      ri = mi - 1
    else:
      li = mi + 1
  return -1


def test_case1():
  nums = [-1,0,3,5,9,12]
  target = 9
  expected_result = 4
  assert expected_result == answer(nums, target)


def test_case2():
  nums = [-1,0,3,5,9,12]
  target = 2
  expected_result = -1
  assert expected_result == answer(nums, target)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])
