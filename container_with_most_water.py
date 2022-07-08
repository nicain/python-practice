"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

source_url = 'https://leetcode.com/problems/container-with-most-water/'

card_url = None


def answer(H):
  hwm = float('-inf')
  li, ri = 0, len(H)-1
  while li < ri:
    width = ri-li
    hwm = max(hwm, min(H[li], H[ri])*width)
    if H[li] <= H[ri]:
      li += 1
    else:
      ri -=1
  return hwm


class Solution:
    def maxArea(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1():
  args = ([1,8,6,2,5,4,8,3,7],)
  expected_result = 49
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ([1,1],)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])