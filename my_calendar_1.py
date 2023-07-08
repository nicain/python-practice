class Node:

  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.left = None
    self.right = None
    self.max = end

  @property
  def val(self):
    return self.start


def add_node(cnode, new_node):
  if not cnode: 
    return new_node

  if new_node.val < cnode.val:
    cnode.left = add_node(cnode.left, new_node)
  else:
    cnode.right = add_node(cnode.right, new_node)

  cnode.max = max(cnode.max, new_node.max)
  return cnode

def search(cnode, start, end):
  if not cnode: 
    return False

  if min(cnode.end, end) - max(cnode.start, start) > 0:
    return True

  if cnode.left and (start < cnode.left.max):
    result = search(cnode.left, start, end)
    if result:
      return True
  else:
    result = search(cnode.right, start, end)
    if result:
      return True
  
  return False


class MyCalendar:

  def __init__(self):
    self.root = None
      

  def book(self, start, end):
    if not self.root:
      self.root = Node(start, end)
      return True
    
    if search(self.root, start, end):
      return False

    add_node(self.root, Node(start, end))
    return True