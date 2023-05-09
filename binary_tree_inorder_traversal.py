"""
Given the root of a binary tree, return the 
inorder traversal of its nodes' values.
"""

source_url = (
  'https://leetcode.com/problems/'
  'binary-tree-inorder-traversal/'
)

card_url = None


def in_order(cnode):
  if not cnode: return None
  
  yield from in_order(cnode.left)
  yield cnode.val
  yield from in_order(cnode.right)


def answer(root):
  return [
    val for val in in_order(root) if val
  ]


class Solution:
  def inorderTraversal(
    self,
    *args,
    **kwargs,
  ):
    return answer(*args, **kwargs)


def test_case1(binary_tree_4):
  args = (binary_tree_4,)
  expected_result = [1,3,2]
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])