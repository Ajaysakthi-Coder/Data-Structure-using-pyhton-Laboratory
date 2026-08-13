class Node:
    def __init__(this,title):
        this.title=title
        this.left=None
        this.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.title,end='- > ')
        inorder(root.right)
def preorder(root):
    if root:
        print(root.title,end='- > ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.title,end='- > ')
def input_tree():
    title=input("Enter node title -1 if no node:")
    if title=='-1':
        return None
    root=Node(title)
    root.left=input_tree()
    root.right=input_tree()
    return root
print("ENTER THE NUMBER -1 AS LONG FOR DOUBLE THE ELEMENTS IN THE TREE TO STOP RECURSTION")    
root=input_tree()
print("Inorder:" ,end =" ")
inorder(root)
print("Preorder:",end  =" ")
preorder(root)
print("Postorder",end =" ")
postorder(root)
print(None)
    
