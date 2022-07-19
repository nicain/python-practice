"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water."""

source_url = 'https://leetcode.com/problems/number-of-islands/'

title = 'Number of Islands'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390413029/edit'

def answer(grid):
  if not grid: return 0

  def dfs(ri, ci):
    nonlocal grid
    if not (0<=ri<len(grid)):
      return
    if not (0<=ci<len(grid[0])):
      return
    if grid[ri][ci] != '1':
      return
    grid[ri][ci] = '#'
    dfs(ri+1, ci)
    dfs(ri-1, ci)
    dfs(ri, ci+1)
    dfs(ri, ci-1)

  count = 0
  for ri in range(len(grid)):
    for ci in range(len(grid[0])):
      if grid[ri][ci] == '1':
        count += 1
        dfs(ri, ci)
  return count




class Solution:
  def numIslands(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1():
  args = ([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
],)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
],)
  expected_result = 3
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])