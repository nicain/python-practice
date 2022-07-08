import pytest

from common import BinaryTreeNode
from values_to_binary_tree_iterative import values_to_binary_tree_iterative


@pytest.fixture
def binary_tree_1():
  values = [10,5,15,3,7,None,18]
  return values_to_binary_tree_iterative(values)


@pytest.fixture
def binary_tree_2():
  values = [10,5,15,3,7,13,18,1,None,6]
  return values_to_binary_tree_iterative(values)
