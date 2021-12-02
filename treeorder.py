
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



def buildTree2(preorder,inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree2(preorder, inorder[0:ind])
        root.right = buildTree2(preorder, inorder[ind+1:])
        return root

def post(root):
    ret = []
    stack=[root]
    while len(stack)>0:
        out=stack.pop()
        ret.append(out.val)
        if out.left:
            stack.append(out.left)
        if out.right:
            stack.append(out.right)
        
    ret.reverse()
        
    return ret

def post_traverse(node):
    if node == None:
        yield ()
    yield from post_traverse(node.left) if node.left is not None else ()
    
    yield from post_traverse(node.right) if node.right is not None else ()
    yield node.val


import sys 

def main():
    sys.setrecursionlimit(15000)
    _ , preorder , postorder , inorder = [ x.split() for x in sys.stdin.readlines()]
    res = buildTree2(preorder,inorder)
    res = post_traverse(res)
    X = [x for x in res if x is not None]
    if X == postorder:
        print("yes")
    else:
        print("no")
main()
