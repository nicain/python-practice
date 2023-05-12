"""
Given an array of meeting time intervals 
intervals where intervals[i] = 
[starti, endi], return the minimum number 
of conference rooms required.
"""

source_url = (
  'https://leetcode.com/problems/'
  'meeting-rooms-ii/'
)


title = (
  'Meeting Rooms II'
)


import heapq


def answer(intervals):
  if not intervals: return 0
  intervals.sort(key=lambda x:x[0])
  room_heap = []
  heapq.heappush(room_heap, intervals[0][1])
  for start, end in intervals[1:]:
    if room_heap[0] <= start:
      heapq.heappop(room_heap)
    heapq.heappush(room_heap, end)
  return len(room_heap)