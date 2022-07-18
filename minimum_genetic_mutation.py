"""A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank."""

source_url = 'https://leetcode.com/problems/minimum-genetic-mutation/'

title = 'Minimum Genetic Mutation'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390410723/edit'

import collections

def get_all_mutations(seq):
  mutant_list = []
  for ci, char in enumerate(seq):
    for new_char in 'ACGT':
      if new_char == char:
        continue
      new_seq = seq[:ci]+new_char+seq[ci+1:]
      mutant_list.append(new_seq)
  return mutant_list

def answer(start, end, bank):
  bank, seen = set(bank), set()

  def get_all_valid_mutations(seq):
    return [m for m in get_all_mutations(seq) 
      if m in bank]

  node_list = collections.deque([(start, 0)])
  while node_list:
    cnode = node_list.popleft()
    if cnode[0] in seen:
      continue
    if cnode[0] == end:
      return cnode[1]
    seen.add(cnode[0])
    for new_node in get_all_valid_mutations(
        cnode[0]):
      node_list.append((new_node, cnode[1]+1))
  return -1


class Solution:
  def minMutation(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1():
  args = ("AACCGGTT", "AACCGGTA", ["AACCGGTA"],)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
  expected_result = 2
  result = answer(*args)
  assert expected_result == result


def test_case3():
  args = ("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"])
  expected_result = 3
  result = answer(*args)
  assert expected_result == result


def test_case4():
  args = ("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])
  expected_result = 4
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])