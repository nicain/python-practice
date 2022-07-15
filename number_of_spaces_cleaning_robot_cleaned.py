"""A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object. The top left corner of the room will be empty in all test cases.

A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it.

Return the number of clean spaces in the room if the robot runs indefinetely."""

source_url = 'https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/'

title = 'Number of Spaces Cleaning Robot Cleaned'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390224923/edit'


def turn_right(vec):
  if vec == (1,0):
    return 0,-1
  elif vec == (0,-1):
    return -1,0
  elif vec == (-1,0):
    return 0,1
  elif vec == (0,1):
    return 1,0
  else:
    raise RuntimeError


def answer(room):

  num_cleaned = 0
  ri, ci = 0, 0
  vec = (1,0)
  visited = set()
  while (ri, ci, vec) not in visited:
    visited.add((ri, ci, vec))
    if room[ri][ci] == 0:
      room[ri][ci] = 'C'
      num_cleaned += 1


    ri_pre, ci_pre = ri-vec[1], ci+vec[0]
    if ri_pre<0 or ri_pre>=len(room) or ci_pre<0 or ci_pre>=len(room[0]):
      vec = turn_right(vec)
      continue
    if room[ri_pre][ci_pre] == 1:
      vec = turn_right(vec)
      continue
    ri, ci = ri_pre, ci_pre
  return num_cleaned


class Solution:
  def numberOfCleanRooms(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1():
  args = ([[0,0,0],[1,1,0],[0,0,0]],)
  expected_result = 7
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ([[0,1,0],[1,0,0],[0,0,0]],)
  expected_result = 1
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])