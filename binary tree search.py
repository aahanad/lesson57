
class TreeNode():
    def __init__(self,key):
        self.node_data=key
        self.right=None
        self.left=None
list=[]
def in_order(root):
    if root.left != None:
        in_order(root.left)
    print(root.node_data)
    list.append(root.node_data)
    if root.right != None:
        in_order(root.right)


def insert(root,k):
    if root==None:
        return TreeNode(k)
    if root.node_data>k:
        root.left=insert(root.left,k)
    else:
        root.right=insert(root.right,k)
    return root
def search(root,k):
    if root.node_data==k:
        return True
    elif root.node_data>k and root.left!=None:
        return search(root.left,k)
    elif root.node_data<k and root.right!=None:
        return search(root.right,k)
    else:
        return False
def find_min(root):
    current=root
    while current.left is not None:
        current=current.left
    return current
def delete(root,key):
    if root is None:
        return root
    if key<root.node_data:
        root.left=delete(root.left,key)
    elif key>root.node_data:
        root.right=delete(root.right,key)
    #node with only one child or no child
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.right
            root=None
            return temp
        temp=find_min(root.right)
        root.node_data=temp.node_data
        root.right=delete(root.right,temp.node_data)
    return root
root=None
root=insert(root,63)
root=insert(root,78)
root=insert(root,28)
root=insert(root,45)
root=insert(root,13)
root=insert(root,90)
root=insert(root,67)
root=insert(root,35)
find_min(root)
root=delete(root,90)
in_order(root)
print(list[0])
print(list[-1])
print(find_min(root).node_data)
found=search(root,90)
if found ==True:
    print(" your number has been found!")
else:
    print("you number was not found:(")
