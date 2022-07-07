"""Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead."""

source_url = 'https://leetcode.com/problems/minimum-size-subarray-sum/'

card_url = None

import math


def answer(target, nums):
  li = 0
  lwm = float('inf')
  tot = 0
  for ri in range(len(nums)):
    tot += nums[ri]
    while tot >= target:
      lwm = min(lwm, ri - li + 1)
      tot, li = tot-nums[li], li+1
  return lwm if math.isfinite(lwm) else 0


class Solution:
    def minSubArrayLen(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1():
  args = (7, [2,3,1,2,4,3])
  expected_result = 2
  assert expected_result == answer(*args)

def test_case2():
  args = (4, [1,4,4])
  expected_result = 1
  assert expected_result == answer(*args)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])