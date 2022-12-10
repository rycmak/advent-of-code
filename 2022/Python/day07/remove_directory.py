import TreeNode

root_node = TreeNode.TreeNode(name = "/", file_type = "dir")

def increase_parents_dirs_sizes(child_node, size):
  dir = child_node.parent
  dir.size += size
  if dir == root_node:
    return
  increase_parents_dirs_sizes(dir, size)

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

total_disk_space = 70000000
space_required = 30000000
space_available = total_disk_space - root_node.size
space_to_delete = space_required - space_available

nodes_to_visit = [root_node]
big_dirs = []
while nodes_to_visit:
  node = nodes_to_visit[0]
  if (node.file_type == "dir" and node.size >= space_to_delete):
    big_dirs.append(node.size)
  nodes_to_visit.extend([child for child in node.children if child.file_type == "dir"])
  nodes_to_visit.pop(0)

big_dirs.sort()
print(f"Smallest size of directory to delete is {big_dirs[0]}")