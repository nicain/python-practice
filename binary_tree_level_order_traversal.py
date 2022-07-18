"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""

source_url = 'https://leetcode.com/problems/binary-tree-level-order-traversal/'

title = 'Binary Tree Level Order Traversal'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390411060/edit'

import collections

def answer(root):

  if not root: return []

  traversal = collections.defaultdict(list)
  node_list = collections.deque([(root, 0)])
  while node_list:
    cnode, depth = node_list.popleft()
    traversal[depth].append(cnode.val)
    if cnode.left:
      node_list.append((cnode.left, depth+1))
    if cnode.right:
      node_list.append((cnode.right, depth+1))

  result = []
  cdepth = 0
  while traversal:
    result.append(traversal.pop(cdepth))
    cdepth += 1
  
  return result


class Solution:
    def levelOrder(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_13):
  args = (binary_tree_13,)
  expected_result = [[3],[9,20],[15,7]]
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])