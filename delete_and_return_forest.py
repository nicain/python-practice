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


def get_new_roots(root, to_delete):
  to_delete = set(to_delete)
  new_roots = set()

  def traverse(cnode, parent=None):
    nonlocal to_delete, new_roots
    if not cnode: return

    if (parent.val in to_delete) and (cnode.val not in to_delete):
      new_roots.add(cnode)

    traverse(cnode.left, parent=cnode)
    traverse(cnode.right, parent=cnode)
  traverse(root.left, root)
  traverse(root.right, root)

  if root.val not in to_delete:
    new_roots.add(root)

  return new_roots

def answer(root, to_delete):

  new_roots = get_new_roots(root, to_delete)

  def traverse_and_prune(cnode):
    nonlocal to_delete, new_roots
    if not cnode: return

    if (cnode.left is not None) and (cnode.left.val in to_delete):
      cnode.left = None
    if (cnode.right is not None) and (cnode.right.val in to_delete):
      cnode.right = None

    traverse_and_prune(cnode.left)
    traverse_and_prune(cnode.right)

  for new_root in new_roots:
    traverse_and_prune(new_root)

  return new_roots