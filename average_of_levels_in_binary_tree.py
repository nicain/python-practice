"""Given the root of a binary tree, return the average value of the nodes on each level in the form of an array."""

source_url = 'https://leetcode.com/problems/average-of-levels-in-binary-tree/'

title = 'Average of Levels in Binary Tree'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390411484/edit'


def answer(root):

  depth_sum_dict = {}
  depth_count_dict = {}

  def traverse(cnode, depth=0):
    nonlocal depth_sum_dict, depth_count_dict
    if not cnode:
      return
    traverse(cnode.left, depth=depth+1)
    traverse(cnode.right, depth=depth+1)
    depth_sum_dict[depth] = depth_sum_dict.get(depth,0)+cnode.val
    depth_count_dict[depth] = depth_count_dict.get(depth,0)+1
  traverse(root)

  result = [None]*len(depth_sum_dict)
  for depth in range(len(depth_sum_dict)):
    result[depth] = depth_sum_dict[depth]/depth_count_dict[depth]
  return result


class Solution:
  def averageOfLevels(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1(binary_tree_13):
  args = (binary_tree_13,)
  expected_result = [3.00000,14.50000,11.00000]
  result = answer(*args)
  assert expected_result == result


def test_case1(binary_tree_14):
  args = (binary_tree_14,)
  expected_result = [3.00000,14.50000,11.00000]
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])