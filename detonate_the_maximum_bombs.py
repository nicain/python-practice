"""
You are given a list of bombs. The range of 
a bomb is defined as the area where its 
effect can be felt. This area is in the 
shape of a circle with the center as the 
location of the bomb.

The bombs are represented by a 0-indexed 2D 
integer array bombs where 
bombs[i] = [xi, yi, ri]. xi and yi denote 
the X-coordinate and Y-coordinate of the 
location of the ith bomb, whereas ri denotes 
the radius of its range.

You may choose to detonate a single bomb. 
When a bomb is detonated, it will detonate 
all bombs that lie in its range. These bombs 
will further detonate the bombs that lie in 
their ranges.

Given the list of bombs, return the maximum 
number of bombs that can be detonated if you 
are allowed to detonate only one bomb.
"""

source_url = (
  'https://leetcode.com/problems/'
  'detonate-the-maximum-bombs'
)


title = (
  'Detonate the Maximum Bombs'
)

import math


class Bomb:

  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.children = set()
    self.chain_count = None

  def will_trigger(self, other):
    return math.sqrt(
      (self.x - other.x)**2 +
      (self.y - other.y)**2
    ) <= self.radius


def answer(bombs):

  bomb_list = [Bomb(*args) for args in bombs]
  for b1 in bomb_list:
    for b2 in bomb_list:
      if b1 == b2: continue
      if b1.will_trigger(b2):
        b1.children.add(b2)

  hwm = float('-inf')
  cache={}
  def compute_desc(bomb):
    nonlocal cache, hwm

    if bomb in cache: return cache[bomb]
    desc = set()
    bfs_rem = set(bomb.children)
    visited = set([bomb])
    while bfs_rem:
      curr_desc = bfs_rem.pop() 
      visited.add(curr_desc)
      desc.add(curr_desc)
      for b2 in curr_desc.children:
        if b2 not in visited:
          bfs_rem.add(b2)

    cache[bomb] = desc
    hwm = max(hwm, len(desc))
    return desc


  for bomb in bomb_list:
    compute_desc(bomb)
  return hwm+1