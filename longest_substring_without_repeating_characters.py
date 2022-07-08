"""Given a string s, find the length of the longest substring without repeating characters."""

source_url = 'https://leetcode.com/problems/longest-substring-without-repeating-characters/'

card_url = 'https://www.brainscape.com/decks/11570817/cards/389103833/edit'


def answer(s):
  if not s: return 0
  count = {}
  hwm = float('-inf')
  li = 0
  for ci, c in enumerate(s):
    if c in count:
      li = max(count[c]+1, li)
    count[c] = ci
    hwm = max(hwm, ci - li + 1)
  return hwm


class Solution:
    def lengthOfLongestSubstring(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case0():
  args = ("abba",)
  expected_result = 2
  result = answer(*args)
  assert expected_result == result

def test_case1():
  args = ("abcabcbb",)
  expected_result = 3
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ("bbbbb",)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


def test_case3():
  args = ("pwwkew",)
  expected_result = 3
  result = answer(*args)
  assert expected_result == result


def test_case4():
  args = ("dvdf",)
  expected_result = 3
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])