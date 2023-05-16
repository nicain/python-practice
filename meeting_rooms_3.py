"""
You are given an integer n. There are n 
rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings 
where meetings[i] = [starti, endi] means 
that a meeting will be held during the 
half-closed time interval [starti, endi). 
All the values of starti are unique.

Meetings are allocated to rooms in the 
following manner:

Each meeting will take place in the unused 
room with the lowest number.
If there are no available rooms, the meeting
will be delayed until a room becomes free. 
The delayed meeting should have the same 
duration as the original meeting.
When a room becomes unused, meetings that
have an earlier original start time should 
be given the room.
Return the number of the room that held the 
most meetings. If there are multiple rooms, 
return the room with the lowest number.

A half-closed interval [a, b) is the 
interval between a and b including a and 
not including b.
"""

source_url = (
  'https://leetcode.com/problems/'
  'meeting-rooms-iii/'
)


title = (
  'Meeting Rooms III'
)


import math
import heapq
from collections import Counter


class Room:

  def __init__(self, idx, hwm):
    self.idx = idx
    self.set_free()
    self._hwm = hwm
    self._count = 0

  def __lt__(self, other):
    if self.end == other.end:
      return self.idx < other.idx
    return self.end < other.end

  def use_until(self, end):
    self._end = end
    self._count += 1
    self._hwm.update(self._count, self)

  @property
  def end(self):
    return self._end

  def set_free(self):
    self._end = -1


class HighWaterMark:

  def __init__(self):
    self.val = float('-inf')
    self.idx = None

  def update(self, val, obj):
    if val > self.val:
      self.val = val
      self.idx = obj.idx
    elif val == self.val:
      self.idx = min(obj.idx, self.idx)

class RoomHeap:

  def __init__(self, N, hwm=None):
    self._rooms = [
      Room(ri, hwm) for ri in range(N)
    ]

  def __len__(self):
    return len(self._rooms)

  def push(self, room):
    heapq.heappush(self._rooms, room)

  def pop(self):
    return heapq.heappop(self._rooms)

  def peek(self):
    return self._rooms[0]

def answer(n, meetings):
  meetings.sort(key=lambda x: x[0])
  hwm = HighWaterMark()
  unoccupied = RoomHeap(n, hwm)
  occupied = RoomHeap(0)
  for start, end in meetings:
    while (
        occupied and
        occupied.peek().end <= start
      ):
      room = occupied.pop()
      room.set_free()
      unoccupied.push(room)
    if len(unoccupied) > 0:
      room = unoccupied.pop()
      room.use_until(end)
    else:
      room = occupied.pop()
      room.use_until(room.end + end - start)
    occupied.push(room)
  return hwm.idx