import os

class TreeNode:
  def __init__(self, name):
    self.name = name
    self.children = {}
    self.value = None

class PathTree:
  def __init__(self):
    self.root = TreeNode("")

  def insert(self, path, value):
    if not os.path.isabs(path):
      raise ValueError("Path must be an absolute path")

    current_node = self.root
    
    path_parts = path.split(os.path.sep)

    for part in path_parts:
      if part not in current_node.children:
        current_node.children[part] = TreeNode(part)
      current_node = current_node.children[part]

    current_node.value = value

  def get(self, path):
    if not os.path.isabs(path):
      raise ValueError("Path must be an absolute path")

    current_node = self.root
    path_parts = path.split(os.path.sep)

    for part in path_parts:
      if part not in current_node.children:
        return None
      current_node = current_node.children[part]

    return current_node.value