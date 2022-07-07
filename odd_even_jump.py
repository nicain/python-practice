"""You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.
"""

source_url = 'https://leetcode.com/problems/odd-even-jump/'

card_url = 'https://www.brainscape.com/decks/11570817/cards/389103464/edit'

from typing import List


class Node:
  def __init__(self, val, idx) -> None:
     self.val = val
     self.idx = idx
     self.odd_jump_hit = None
     self.even_jump_hit = None


def answer(arr: List[int]) -> int:
  hit_count = 0
  sorted_arr = []
  for idx_rev, val_pre in enumerate(arr[::-1]):
    idx = len(arr)-1-idx_rev
    curr_node = Node(val_pre, idx)
    if idx_rev == 0:
      curr_node.odd_jump_hit = True
      curr_node.even_jump_hit = True
      hit_count += 1
      sorted_arr.append(curr_node)
      continue
    li, ri = 0, len(sorted_arr)
    while li < ri:
        mi = (li + ri) // 2
        if curr_node.val < sorted_arr[mi].val:
            ri = mi
        else:
            li = mi + 1
    

    if li-1 >= 0 and curr_node.val == sorted_arr[li-1].val:
      replace_idx = li-1

      # Odd jump, i.e. right of replace_idx:
      potential_landing_idx = replace_idx
      if potential_landing_idx <= len(sorted_arr)-1:
        landing_node = sorted_arr[potential_landing_idx]
        curr_node.odd_jump_hit = landing_node.even_jump_hit
        if curr_node.odd_jump_hit:
          hit_count += 1
      else:
        curr_node.odd_jump_hit = False

      # Even jump, i.e. left of replace_idx:
      potential_landing_idx = replace_idx
      if 0 <= potential_landing_idx:
        landing_node = sorted_arr[potential_landing_idx]
        curr_node.even_jump_hit = landing_node.odd_jump_hit
      else:
        curr_node.even_jump_hit = False
      sorted_arr[replace_idx] = curr_node
    else:
      insert_idx = li

      # Odd jump, i.e. right
      potential_landing_idx = li
      if potential_landing_idx <= len(sorted_arr)-1:
        landing_node = sorted_arr[potential_landing_idx]
        # print(sorted_arr, potential_landing_idx, landing_node)
        curr_node.odd_jump_hit = landing_node.even_jump_hit
        if curr_node.odd_jump_hit:
          hit_count += 1
      else:
        curr_node.odd_jump_hit = False

      # Even jump, left
      potential_landing_idx = insert_idx-1
      if potential_landing_idx >= 0:
        landing_node = sorted_arr[potential_landing_idx]
        curr_node.even_jump_hit = landing_node.odd_jump_hit
      else:
        curr_node.even_jump_hit = False
      sorted_arr.insert(insert_idx, curr_node)
  return hit_count

class Solution:
    def oddEvenJumps(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1():
  args =([10,13,12,14,15],)
  expected_result = 2
  assert expected_result == answer(*args)


def test_case2():
  args =([2,3,1,1,4],)
  expected_result = 3
  assert expected_result == answer(*args)


def test_case3():
  args =([5,1,3,4,2],)
  expected_result = 3
  assert expected_result == answer(*args)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])
