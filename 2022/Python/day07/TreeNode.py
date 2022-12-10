class TreeNode:
  def __init__(self, name, file_type, size=0):
    self.name = name # data
    self.children = []
    self.parent = None
    self.file_type = file_type
    self.size = size

  def add_child(self, child_node):
    child_node.parent = self
    self.children.append(child_node)
  
  def __repr__(self, level=0):
    tree = "\t" * level + repr(self.name) + "  " + repr(self.size) + "\n"
    for child in self.children:
        tree += child.__repr__(level + 1)
    return tree