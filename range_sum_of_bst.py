"""Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high]."""

source_url = 'https://leetcode.com/problems/range-sum-of-bst/'

card_url = None


from common import BinaryTreeNode as TreeNode


def answer(root, low, high):
  def dfs(cnode):
    nonlocal tot
    if cnode:
      if low <= cnode.val and cnode.val <= high:
        tot += cnode.val
      if low < cnode.val:
        dfs(cnode.left)
      if cnode.val < high:
        dfs(cnode.right)
  tot = 0
  dfs(root)
  return tot


class Solution:
    def rangeSumBST(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_1):
  args = (binary_tree_1,7,15)
  expected_result = 32
  result = answer(*args)
  assert expected_result == result


def test_case2(binary_tree_2):
  args = (binary_tree_2,6,10)
  expected_result = 23
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])