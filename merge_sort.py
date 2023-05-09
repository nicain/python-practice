"""
Given an array of integers nums, sort the 
array in ascending order and return it.

You must solve the problem without using 
any built-in functions in O(nlog(n)) time 
complexity and with the smallest space 
complexity possible.
"""

source_url = (
  'https://leetcode.com/problems/'
  'sort-an-array/'
)

title = (
  'Sort an Array'
)


def merge(left, right):
  output = []
  li = ri = 0
  while li < len(left) and ri < len(right):
    if left[li] < right[ri]:
      output.append(left[li])
      li += 1
    else:
      output.append(right[ri])
      ri += 1
  output += left[li:]
  output += right[ri:]
  return output


def merge_sort(arr):
  if len(arr) == 1: return arr

  mi = len(arr) // 2

  left = merge_sort(arr[:mi])
  right = merge_sort(arr[mi:])

  return merge(left, right)


def answer(arr):
  return array_to_bst(arr)


class Solution:
  def sortedArrayToBST(
    self,
    *args,
    **kwargs
  ): return answer(*args, **kwargs)