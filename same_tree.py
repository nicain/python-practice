"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

source_url = 'https://leetcode.com/problems/same-tree/'

title = 'Same Tree'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390158358/edit'


def answer(p, q):
  if not p and not q:
      return True
  if not q or not p:
      return False
  if p.val != q.val:
      return False
  right_tree = answer(p.right, q.right)
  left_tree = answer(p.left, q.left)
  return left_tree and right_tree


class Solution:
    def isSameTree(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_3, binary_tree_4):
  args = (binary_tree_3, binary_tree_4)
  expected_result = False
  result = answer(*args)
  assert expected_result == result


def test_case2(binary_tree_3):
  args = (binary_tree_3, binary_tree_3)
  expected_result = True
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])