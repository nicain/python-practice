"""
You are given the root of a binary tree with
n nodes. Each node is assigned a unique 
value from 1 to n. You are also given an 
array queries of size m.

You have to perform m independent queries 
on the tree where in the ith query you do 
the following:

Remove the subtree rooted at the node with 
the value queries[i] from the tree. It is 
guaranteed that queries[i] will not be equal
to the value of the root.

Return an array answer of size m where 
answer[i] is the height of the tree after 
performing the ith query.

Note:

The queries are independent, so the tree 
returns to its initial state after each 
query.
The height of a tree is the number of edges
in the longest simple path from the root to
some node in the tree.
"""

source_url = (
  'https://leetcode.com/problems/'
  'height-of-binary-tree-after-subtree-removal-queries/'
)

title = (
  'Height of Binary Tree After '
  'Subtree Removal Queries'
)

import itertools as it


def answer(root, queries):

  cache = {}
  def height(cnode):
    nonlocal cache
    if cnode in cache: return cache[cnode]
    if cnode is None: return -1
    h = 1 + max(
      height(cnode.left), 
      height(cnode.right),
    )
    cache[cnode] = h
    return cache[cnode]

  result = {}
  def dfs(cnode, depth, parent_max):
    nonlocal result
    if not cnode: return
    result[cnode.val] = parent_max
    for a, b in it.permutations(
      [cnode.left, cnode.right]
    ):
      sibling_max = depth+1+height(b)
      dfs(
        a,
        depth+1, 
        max(parent_max, sibling_max),
      )

  dfs(root, 0, 0)
  return [result[q] for q in queries]