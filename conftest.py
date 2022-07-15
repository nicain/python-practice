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


@pytest.fixture
def binary_tree_3():
  values = [7,3,15,None,None,9,20]
  return values_to_binary_tree_iterative(values)


@pytest.fixture
def binary_tree_4():
  values = [1,None,2,None, None, 3, None]
  return values_to_binary_tree_iterative(values)


@pytest.fixture
def binary_tree_5():
  values = [4,2,6,1,3]
  return values_to_binary_tree_iterative(values)


@pytest.fixture
def binary_tree_6():
  values = [1,0,48,None,None,12,49]
  return values_to_binary_tree_iterative(values)


@pytest.fixture
def binary_tree_7():
  values = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
  return values_to_binary_tree_iterative(values)