"""
Given the root of a binary tree, each node 
in the tree has a distinct value.

After deleting all nodes with a value in 
to_delete, we are left with a forest 
(a disjoint union of trees).

Return the roots of the trees in the 
remaining forest. You may return the result 
in any order.
"""

source_url = (
  'https://leetcode.com/problems/'
  'delete-nodes-and-return-forest'
)


title = (
  'Delete Nodes And Return Forest'
)


def answer(root, to_delete):
  to_delete = set(to_delete)
  results = []
  if root.val not in to_delete:
    results.append(root)
  prune_list = []
  def delete(cnode, parent=None, side=None):
    nonlocal results, to_delete, prune_list
    if not cnode: return

    if cnode.val in to_delete:
      for x in [cnode.left, cnode.right]:
        if x and x.val not in to_delete:
          results.append(x)
      if parent:
        prune_list.append((parent, side))

    delete(cnode.left, cnode, 'L')
    delete(cnode.right, cnode, 'R')
  delete(root)

  for parent, side in prune_list:
    if side == 'L': parent.left = None
    elif side == 'R': parent.right = None

  return results