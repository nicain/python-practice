"""
Given a string s containing just the 
characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same 
type of brackets.
Open brackets must be closed in the correct
order.
Every close bracket has a corresponding
open bracket of the same type.
"""

source_url = (
  'https://leetcode.com/problems/'
  'valid-parentheses/'
)

title = (
  'Valid Parentheses'
)

D = {'(':')', '[':']', '{':'}'}
Dr = {val:key for key, val in D.items()}

def answer(s):
  stack = []
  for c in s:
    if c in D:
      stack.append(c)
      continue
      
    if (c in Dr) and (
        len(stack) == 0 or
        stack.pop() != Dr[c]
    ):
      return False
  return True if len(stack) == 0 else False

class Solution:
  def isValid(
    self,
    *args,
    **kwargs
  ): return answer(*args, **kwargs)
