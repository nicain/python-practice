"""Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res."""

source_url = 'https://leetcode.com/problems/print-binary-tree/'

title = 'Print Binary Tree'

card_url = None


def get_width(height):
  if height == 1:
    return 1
  return 2*get_width(height-1)+1


def answer(root):
  coord_dict = {}
  def traverse(cnode, coord=''):
    nonlocal coord_dict
    if not cnode:
      return None
    coord_dict[coord] = cnode.val
    left_result = traverse(cnode.left, coord=coord+'L')
    right_result = traverse(cnode.right, coord=coord+'R')
  traverse(root)
  height = 1+max([len(coord) for coord in coord_dict])
  width = get_width(height)
  
  result = []
  for _ in range(height):
    result.append([""]*width)

  for coord, val in coord_dict.items():
    curr_depth = len(coord)
    curr_width = width
    ci = int((curr_width-1)/2)
    for side in coord:
      subblock_width = int((curr_width-1)/2)
      if side == 'L':
        ci = ci - (int((subblock_width-1)/2)+1)
      else:
        ci = ci + (int((subblock_width-1)/2)+1)
      curr_width = int((curr_width-1)/2)+1
    result[curr_depth][ci] = str(val)

  return result


def print_tree(root):
  result = answer(root)

  width_hwm = float('-inf')
  for row in result:
    for val in row:
      width_hwm = max(width_hwm, len(val))
  cstr = ''
  for row in result:
    new_row = []
    for val in row:
      if val == '':
        ival = ' '*width_hwm
      else:
        missing_wspace = width_hwm-len(val)
        padding_l = (missing_wspace//2)*" "
        padding_r = (missing_wspace-missing_wspace//2)*" "
        ival = padding_l+val+padding_r
        assert len(ival) == width_hwm
      new_row.append(ival)
    cstr += ''.join(new_row)+'\n'
  print(cstr)


class Solution:
    def printTree(self, *args, **kwargs):
        return answer(*args, **kwargs)


def test_case1(binary_tree_9):
  args = (binary_tree_9,)
  expected_result = [
    ["","","","1","","",""],
    ["","2","","","","3",""],
    ["","","4","","","",""],
  ]
  result = answer(*args)
  assert expected_result == result
  print(result)


def test_case2(binary_tree_10):
  args = (binary_tree_10,)
  expected_result = [
    ["","1",""],
    ["2","",""],
  ]
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])