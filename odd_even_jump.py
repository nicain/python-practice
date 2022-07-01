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

def answer(arr: List[int]) -> int:
    hit_set = set()
    for starting_ind in range(len(arr)-1):
      parity = 0
      print()
      print(starting_ind)
      curr_ind = starting_ind
      while True:
        parity = 1-parity
        print(parity, curr_ind)
        if parity == 1:
          lwm = float('inf')
          lwmi = None
          for potential_jump_ind in range(1+curr_ind, len(arr)):
            if arr[potential_jump_ind] >= arr[curr_ind]:
              if arr[potential_jump_ind] < lwm:
                lwmi = potential_jump_ind
                lwm = arr[potential_jump_ind]
          if lwmi == len(arr)-1:
            hit_set.add(starting_ind)
            print('HIT')
            break
          elif not lwmi:
            print('MISS-a')
            break
          else:
            curr_ind = lwmi
        else:
          hwm = float('-inf')
          hwmi = None
          for potential_jump_ind in range(1+curr_ind, len(arr)):
            if arr[potential_jump_ind] <= arr[curr_ind]:
              if arr[potential_jump_ind] > hwm:
                hwmi = potential_jump_ind
                hwm = arr[potential_jump_ind]
          if hwmi == len(arr)-1:
            hit_set.add(starting_ind)
            print('HIT')
            break
          elif not hwmi:
            print('MISS-b')
            break
          else:
            curr_ind = hwmi

    return len(hit_set)+1


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
  # import pytest
  # pytest.main([__file__])
  test_case3()