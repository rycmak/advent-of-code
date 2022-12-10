import TreeNode

def increase_parents_dirs_sizes(child_node, size):
  dir = child_node.parent
  dir.size += size
  if dir == root_node:
    return
  increase_parents_dirs_sizes(dir, size)

root_node = TreeNode.TreeNode(name = "/", file_type = "dir")
current_node = root_node

file = open("input.txt", 'r')
for line in file:
  if line.startswith("$ cd"):
    dir = line.strip()[5:]
    if dir == "/":
      current_node = root_node
    elif dir == "..":
      current_node = current_node.parent
    else:
      current_node = [n for n in current_node.children if 
                        (n.name == dir and n.file_type == "dir")][0]
  elif line.startswith("$ ls"):
    continue
  else: # listing contents of current directory
    if line.startswith("dir"):  # contains another directory
      dir_name = line.strip().split()[1]
      current_node.add_child(TreeNode.TreeNode(name = dir_name, file_type = "dir"))
    else: # contains a file
      file_name = line.strip().split()[1]
      file_size = int(line.strip().split()[0])
      file_node = TreeNode.TreeNode(name = file_name, file_type = "file", size = file_size)
      current_node.add_child(file_node)
      increase_parents_dirs_sizes(file_node, file_node.size)

total_dir_size = 0

def sum_total_dir_size(node):
  global total_dir_size
  if (node.file_type == "dir"):
    if node.size <= 100000:
      total_dir_size += node.size
    for child in node.children:
      sum_total_dir_size(child)

sum_total_dir_size(root_node)
print(f"Total size of directories with sizes at most 100000 is {total_dir_size}")