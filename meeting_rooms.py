"""
Given an array of meeting time intervals 
where intervals[i] = [starti, endi], 
determine if a person could attend all 
meetings.
"""

source_url = (
  'https://leetcode.com/problems/'
  'meeting-rooms/'
)


title = (
  'Meeting Rooms'
)


def answer(intervals):
  intervals.sort(key=lambda x:x[0])
  for ci_m1, (start, end) in enumerate(
    intervals[1:]
  ):
    if start < intervals[ci_m1][1]:
      return False
  return True


from collections import Counter


def answer_2(intervals):
  if not intervals: return True

  start_cnt, end_cnt = [
    Counter(x) for x in zip(*intervals)
  ]

  for cnt in [start_cnt, end_cnt]:
    if max(cnt.values()) > 1: return False

  m = min(start_cnt.keys())
  M = max(end_cnt.keys())
  tracker, ch = 0, m
  while ch < M:
    print(tracker, ch)
    if ch in start_cnt:
      tracker += 1
    if ch in end_cnt:
      tracker -= 1
    if tracker > 1:
      return False
    ch += 1
  return True