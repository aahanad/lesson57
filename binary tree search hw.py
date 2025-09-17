class TreeNode:
    def __init__(self, node_data):
        self.node_data = node_data
        self.left = None
        self.right = None

def post_order(root):
    if root.left is not None:
        post_order(root.left)
    if root.right is not None:
        post_order(root.right)
    print(root.node_data)

def pre_order(root):
    print(root.node_data)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)

def in_order(root):
    if root.left is not None:
        in_order(root.left)
    print(root.node_data)
    if root.right is not None:
        in_order(root.right)

# 🔍 Function to search for a node
def search_node(root, target):
    if root is None:
        return False
    if root.node_data == target:
        return True
    return search_node(root.left, target) or search_node(root.right, target)

# 🧮 Function to find min and max value in the tree
def find_min_max(root):
    if root is None:
        return (None, None)
    
    min_val = root.node_data
    max_val = root.node_data

    def traverse(node):
        nonlocal min_val, max_val
        if node:
            if node.node_data < min_val:
                min_val = node.node_data
            if node.node_data > max_val:
                max_val = node.node_data
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return (min_val, max_val)

# 🌳 Build the tree
root = TreeNode(77)
root.right = TreeNode(43)
root.right.left = TreeNode(90)
root.left = TreeNode(92)
root.left.left = TreeNode(13)
root.left.left.right = TreeNode(89)
root.right.right = TreeNode(58)
root.left.left.left = TreeNode(72)
root.right.right.right = TreeNode(21)
root.right.right.right.left = TreeNode(37)
root.right.right.right.right = TreeNode(27)

# 🌐 Menu to test features
print("Choose an operation:")
print("1. In-Order Traversal")
print("2. Pre-Order Traversal")
print("3. Post-Order Traversal")
print("4. Search for a Node")
print("5. Print Min and Max")

choice = int(input("Enter choice (1-5): "))

if choice == 1:
    print("In-Order Traversal:")
    in_order(root)
elif choice == 2:
    print("Pre-Order Traversal:")
    pre_order(root)
elif choice == 3:
    print("Post-Order Traversal:")
    post_order(root)
elif choice == 4:
    value = int(input("Enter value to search: "))
    found = search_node(root, value)
    if found:
        print(f"Value {value} found in the tree.")
    else:
        print(f"Value {value} not found in the tree.")
elif choice == 5:
    min_val, max_val = find_min_max(root)
    print(f"Minimum value in the tree: {min_val}")
    print(f"Maximum value in the tree: {max_val}")
else:
    print("Invalid choice.")