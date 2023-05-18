import heapq

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Node:

  def __init__(self, node):
    self.node = node

  def __lt__(self, other):
    return self.val < other.val

  @property
  def val(self):
    return self.node.val

def answer(lists):
  if not len(lists): return None

  heads = [Node(n) for n in lists if n]
  if not heads:
    return None

  def push(next):
    nonlocal heads
    if next:
      heapq.heappush(heads, Node(next))

  heapq.heapify(heads)
  head = root = heapq.heappop(heads).node
  push(head.next)
  while heads:
    popped = heapq.heappop(heads).node
    push(popped.next)
    head.next = popped
    head = popped
  return root