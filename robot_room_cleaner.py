"""You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

Custom testing:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.
"""

source_url = 'https://leetcode.com/problems/robot-room-cleaner/'

title = 'Robot Room Cleaner'

card_url = None

import pytest
class Robot:

  clean_marker = 'X'

  def __init__(self, room, row, col):

    self.room = room
    self.row = row
    self.col = col  
    self.vector_x = 0
    self.vector_y = 1
    self.counter = 0

  def move(self):
    """
    Returns true if the cell in front is open and robot moves into the cell.
    Returns false if the cell in front is blocked and robot stays in the current cell.
    :rtype bool
    """
    self.counter += 1
    if self.vector_x == 0 and self.vector_y == 1:
      new_row = self.row - 1
      new_col = self.col
    elif self.vector_x == 1 and self.vector_y == 0:
      new_row = self.row
      new_col = self.col + 1
    elif self.vector_x == 0 and self.vector_y == -1:
      new_row = self.row + 1
      new_col = self.col
    elif self.vector_x == -1 and self.vector_y == 0:
      new_row = self.row
      new_col = self.col - 1
    else:
      raise RuntimeError

    in_bounds = (
        (0 <= new_row < len(self.room)) 
      and 
        (0 <= new_col < len(self.room[0]))
    )    
    if not in_bounds:
      return False
    if self.room[new_row][new_col] == 0:
      return False
    self.row, self.col = new_row, new_col
    return True 

  def turnLeft(self):
    """
    Robot will stay in the same cell after calling turnLeft/turnRight.
    Each turn will be 90 degrees.
    :rtype void
    """
    self.counter += 1
    if self.vector_x == 0 and self.vector_y == 1:
      self.vector_x, self.vector_y = -1, 0
    elif self.vector_x == -1 and self.vector_y == 0:
      self.vector_x, self.vector_y = 0, -1
    elif self.vector_x == 0 and self.vector_y == -1:
      self.vector_x, self.vector_y = 1, 0
    elif self.vector_x == 1 and self.vector_y == 0:
      self.vector_x, self.vector_y = 0, 1
    else:
      raise RuntimeError

  def turnRight(self):
    """
    Robot will stay in the same cell after calling turnLeft/turnRight.
    Each turn will be 90 degrees.
    :rtype void
    """
    self.counter += 1
    if self.vector_x == 0 and self.vector_y == 1:
      self.vector_x, self.vector_y = 1, 0
    elif self.vector_x == 1 and self.vector_y == 0:
      self.vector_x, self.vector_y = 0, -1
    elif self.vector_x == 0 and self.vector_y == -1:
      self.vector_x, self.vector_y = -1, 0
    elif self.vector_x == -1 and self.vector_y == 0:
      self.vector_x, self.vector_y = 0, 1
    else:
      raise RuntimeError
  

  def clean(self):
    """
    Clean the current cell.
    :rtype void
    """
    self.counter += 1
    self.room[self.row][self.col] = self.clean_marker


class Solution:
    def cleanRoom(self, robot):      

      def probe_forward():
        successful_move_foward = robot.move()
        if not successful_move_foward:
          return False
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        return True

      def probe_left():
        robot.turnLeft()
        successful_move_foward = probe_forward()
        robot.turnRight()
        return successful_move_foward

      def probe_right():
        robot.turnRight()
        successful_move_foward = probe_forward()
        robot.turnLeft()
        return successful_move_foward

      def probe_backward():
        robot.turnLeft()
        robot.turnLeft()
        successful_move_foward = probe_forward()
        robot.turnRight()
        robot.turnRight()
        return successful_move_foward

      visited = set()
      def iterate(ri, ci):
        nonlocal visited
        robot.clean()
        visited.add((ri, ci))
        if (ri+1, ci) not in visited and probe_forward():
          robot.move()
          iterate(ri+1, ci)
          robot.turnLeft()
          robot.turnLeft()
          robot.move()
          robot.turnRight()
          robot.turnRight()
        if (ri-1, ci) not in visited and probe_backward():
          robot.turnLeft()
          robot.turnLeft()
          robot.move()
          robot.turnRight()
          robot.turnRight()
          iterate(ri-1, ci)
          robot.move()
        if (ri, ci-1) not in visited and probe_left():
          robot.turnLeft()
          robot.move()
          robot.turnRight()
          iterate(ri, ci-1)
          robot.turnRight()
          robot.move()
          robot.turnLeft()
        if (ri, ci+1) not in visited and probe_right():
          robot.turnRight()
          robot.move()
          robot.turnLeft()
          iterate(ri, ci+1)
          robot.turnLeft()
          robot.move()
          robot.turnRight()
      iterate(0, 0)


def room_is_clean(room):
  for row in room:
    for val in row:
      if val not in [0,Robot.clean_marker]:
        for row in room:
          print(room)
        return False
  return True


def harness(room, row, col):
  robot = Robot(room, row, col)
  solution = Solution()
  solution.cleanRoom(robot)
  print(robot.counter)
  return room_is_clean(room)


def test_case1():
  args = (
      [
        [1,1,1,1,1,0,1,1],
        [1,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,1,1],
        [0,0,0,1,0,0,0,0],
        [1,1,1,1,1,1,1,1]
        ],
      1, 
      3,
    )
  expected_result = True
  result = harness(*args)
  assert expected_result == result


def test_case2():
  args = (
    [
      [1],
      [1],
    ],0,0,
  )
  expected_result = True
  result = harness(*args)
  assert expected_result == result


@pytest.mark.parametrize("room", 
  (
    [[1]],
    [[1,0]],
    [[1],[0]],
  )
)
def test_robot_1(room):
  row = 0
  col = 0
  robot = Robot(room, row, col)
  for _ in range(4):
    assert not robot.move()
    robot.turnLeft()
  for _ in range(3):
    assert not robot.move()
    robot.turnRight()
  assert not room_is_clean(room)
  robot.clean()
  assert room_is_clean(room)
  robot.clean()
  assert room_is_clean(room)


def test_robot_2():
  room =[[1,1]]
  row = 0
  col = 0
  robot = Robot(room, row, col)
  assert not room_is_clean(room)
  assert not robot.move()
  robot.turnRight()
  assert robot.move()
  assert not robot.move()
  robot.clean()
  assert not room_is_clean(room)
  robot.turnRight()
  assert not robot.move()
  robot.turnRight()
  assert robot.move()
  assert not room_is_clean(room)
  robot.clean()
  assert room_is_clean(room)


if __name__ == "__main__":
  pytest.main([__file__])