"""Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called."""

source_url = 'https://leetcode.com/problems/binary-search-tree-iterator/'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390017989/edit'

import itertools

def in_order_search(cnode):
  if not cnode:
    return
  yield from in_order_search(cnode.left)
  yield cnode.val 
  yield from in_order_search(cnode.right)


class BSTIterator:

    def __init__(self, root):
      self.search_iterator = in_order_search(root)

    def next(self) -> int:
      return next(self.search_iterator)

    def hasNext(self) -> bool:
      try:
          first = next(self.search_iterator)
          self.search_iterator = itertools.chain(
            [first], self.search_iterator)
          return True
      except StopIteration:
          return False


def test_case1(binary_tree_3):
  root = binary_tree_3
  obj = BSTIterator(root)

  result = [
    obj.next(),
    obj.next(),
    obj.hasNext(),
    obj.next(),
    obj.hasNext(),
    obj.next(),
    obj.hasNext(),
    obj.next(),
    obj.hasNext(),
  ]
  expected_result = [3, 7, True, 9, True, 15, True, 20, False]
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])