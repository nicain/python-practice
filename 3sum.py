"""
Given an integer array nums, return all the 
triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i]
nums[j] + nums[k] == 0.

Notice that the solution set must not 
contain duplicate triplets.
"""

source_url = (
  'https://leetcode.com/problems/'
  '3sum/'
)

title = (
  '3Sum'
)
  
import itertools as it


def answer(nums):
  n, z, p = [], [], []
  for num in nums:
    if num < 0: n.append(num)
    elif num == 0: z.append(num)
    elif num > 0: p.append(num)

  res = {(0,0,0)} if len(z) >= 3 else set()
  N, P = set(n), set(p)
  if z:
    for num in P:
      if -num in N:
        res.add((-num, 0, num))

  for (l1, s1), (l2, s2) in it.permutations(
    [(n, N), (p, P)], 2):
    for n1, n2 in combinations(l1, 2):
      n = (n1, n2) if n1 <= n2 else (n2, n1)
      tgt = -(n1+n2)
      if tgt in s2:
        if tgt >= 0:
          res.add((*n, tgt))
        else:
          res.add((tgt, *n))

  return res