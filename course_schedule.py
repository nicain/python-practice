"""
There are a total of numCourses courses you 
have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want 
to take course ai.

For example, the pair [0, 1], indicates that
to take course 0 you have to first take course 1.
Return true if you can finish all courses. 
Otherwise, return false.
"""

source_url = (
  'https://leetcode.com/problems/'
  'course-schedule'
)

title = (
  'Course Schedule'
)

class CycleDetectedError(Exception):
  """Error for cycle detection"""

def answer_wrapped(numCourses, prerequisites):

  edges = {ci:set() for ci in range(numCourses)}
  for src, tgt in prerequisites:
    edges[src].add(tgt)
  
  reached, mark = set(), set()
  def detect_cycles(cnode):
    nonlocal reached, mark
    if cnode in mark:
      raise CycleDetectedError
    
    if cnode in reached:
      return

    mark.add(cnode)
    for child in edges[cnode]:
      detect_cycles(child)
    mark.remove(cnode)
    reached.add(cnode)

  for ci in range(numCourses):
    detect_cycles(ci)


def answer(*args, **kwargs):
  try:
    answer_wrapped(*args, **kwargs)
    return True
  except CycleDetectedError:
    return False