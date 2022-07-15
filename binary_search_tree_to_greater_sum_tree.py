"""Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

source_url = 'https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/'

title  = 'Binary Search Tree to Greater Sum Tree'

card_url = None


from same_tree import answer as same_tree
from print_tree import print_tree


def answer(root):
  prev_sum = 0
  def rev_in_order(cnode):
    nonlocal prev_sum
    if not cnode:
      return
    rev_in_order(cnode.right)
    cnode.val = cnode.val + prev_sum
    prev_sum = cnode.val
    rev_in_order(cnode.left)
  rev_in_order(root)
  return root


class Solution:
    def bstToGst(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_7, binary_tree_8):
  args = (binary_tree_7,)
  expected_tree_root = binary_tree_8
  result = answer(*args)
  print('======================')
  print_tree(result)
  print('----------------------')
  print_tree(expected_tree_root)
  print('======================')
  assert same_tree(expected_tree_root, result)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])