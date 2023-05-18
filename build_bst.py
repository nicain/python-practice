class Node:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def add_node(cnode, new_node):
  if new_node.val < cnode.val:
    if cnode.left:
      return add_node(cnode.left, new_node)
    else:
      cnode.left = new_node
    return
  else:
    if cnode.right:
      return add_node(cnode.right, new_node)
    else:
      cnode.right = new_node
    

root = None
for ii, val in enumerate([15, 10, 5, 12, 30, 16, 35]):
  new_node = Node(val)
  if ii == 0:
    root = new_node
    continue
  add_node(root, new_node)