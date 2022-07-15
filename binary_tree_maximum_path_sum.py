"""A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path."""

source_url = 'https://leetcode.com/problems/binary-tree-maximum-path-sum/'

title = 'Binary Tree Maximum Path Sum'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390226913/edit'


def answer(root):
  hwm = float('-inf')
  def traverse(cnode):
    nonlocal hwm
    if not cnode:
      return 0
    left_sum = traverse(cnode.left)
    right_sum = traverse(cnode.right)
    hwm = max(hwm, left_sum+right_sum+cnode.val)
    best_sum = max(left_sum, right_sum)
    return max(0, best_sum+cnode.val)
  traverse(root)
  return hwm


class Solution:
  def maxPathSum(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1(binary_tree_11):
  args = (binary_tree_11,)
  expected_result = 6
  result = answer(*args)
  assert expected_result == result


def test_case2(binary_tree_12):
  args = (binary_tree_12,)
  expected_result = 42
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])