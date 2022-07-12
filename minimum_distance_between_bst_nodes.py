"""Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree."""

source_url = 'https://leetcode.com/problems/minimum-distance-between-bst-nodes/'

card_url = None


def answer(root):
  prev = None
  lwm = float('inf')
  def in_order(cnode):
    nonlocal lwm, prev
    if not cnode:
      return
    in_order(cnode.left)
    if prev is not None:
      lwm = min(lwm, cnode.val-prev)
    prev = cnode.val
    in_order(cnode.right)
  in_order(root)
  return lwm
  

class Solution:
    def minDiffInBST(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_5):
  args = (binary_tree_5,)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


def test_case2(binary_tree_6):
  args = (binary_tree_6,)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])