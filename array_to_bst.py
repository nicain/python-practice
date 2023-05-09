"""
Given an integer array nums where the 
elements are sorted in ascending order, 
convert it to a height-balanced binary 
search tree.
"""

source_url = (
  'https://leetcode.com/problems/'
  'average-of-levels-in-binary-tree/'
)

title = (
  'Convert Sorted Array to Binary Search'
  'Tree'
)


# Definition for a binary tree node.
class TreeNode:
  def __init__(self,
    val=0,
    left=None,
    right=None,
  ):
    self.val = val
    self.left = left
    self.right = right


def array_to_bst(arr):
  if not arr: return None
  mi = len(arr)//2
  cnode = TreeNode(val=arr[mi])
  cnode.left = array_to_bst(arr[:mi])
  cnode.right = array_to_bst(arr[mi+1:])
  return cnode


def answer(arr):
  return array_to_bst(arr)


class Solution:
  def sortedArrayToBST(
    self,
    *args,
    **kwargs
  ): return answer(*args, **kwargs)
