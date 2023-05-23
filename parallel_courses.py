"""
You are given an integer n, which indicates 
that there are n courses labeled from 1 to 
n. You are also given an array relations where 
relations[i] = [prevCoursei, nextCoursei], 
representing a prerequisite relationship 
between course prevCoursei and course 
nextCoursei: course prevCoursei has to be 
taken before course nextCoursei.

In one semester, you can take any number of 
courses as long as you have taken all the 
prerequisites in the previous semester for 
the courses you are taking.

Return the minimum number of semesters 
needed to take all courses. If there is no 
way to take all the courses, return -1.
"""

source_url = (
  'https://leetcode.com/problems/'
  'parallel-courses'
)

title = (
  'Parallel Courses'
)


class CycleDetectedError(Exception):
  """Error for cycle detection"""


def answer_wrapped(n, relations):

  deps = {ii:set() for ii in range(1,n+1)}
  for src, tgt in relations:
    deps[tgt].add(src)

  depth = {}
  visited = set()
  def visit(cnode):
    nonlocal depth, visited
    if cnode in visited:
      raise CycleDetectedError
    if cnode in depth: return depth[cnode]

    children_depth = 0
    visited.add(cnode)
    for child in deps[cnode]:
      children_depth = max(children_depth, visit(child))
    visited.remove(cnode)
    depth[cnode] = children_depth + 1
    return depth[cnode]


  hwm = 0
  for node in deps:
    hwm = max(hwm, visit(node))
  return hwm

def answer(*args, **kwargs):
  try:
    return answer_wrapped(*args, **kwargs)
  except CycleDetectedError:
    return -1