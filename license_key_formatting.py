"""You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key."""

source_url = 'https://leetcode.com/explore/interview/card/google/67/sql-2/472/'

card_url = None


def answer(s, k):
  s = s.upper()
  text = s.replace('-','')
  remaining = text
  result = ''
  while remaining:
    remaining, curr_group = remaining[:-k], remaining[-k:]
    result = f'{curr_group}-{result}'
  return result[:-1]


class Solution:
    def licenseKeyFormatting(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1():
  args = ('5F3Z-2e-9-w', 4)
  expected_result = '5F3Z-2E9W'
  assert expected_result == answer(*args)

def test_case2():
  args = ('2-5g-3-J', 2)
  expected_result = '2-5G-3J'
  assert expected_result == answer(*args)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])