
def buildTree(preorder,inorder):
    if not preorder and not inorder: return None
    root = TreeNode(preorder[0])
    d = {node: pos for pos, node in enumerate(inorder)}
    for node in preorder[1:]:
        prev = root
        n = root
        while n:
            prev = n
            if d[node] > d[n.val]:
                n = n.right
            elif d[node] < d[n.val]:
                n = n.left
        if d[prev.val] > d[node]:
            prev.left = TreeNode(node)
        else: 
            prev.right = TreeNode(node)                 
    return root

def checktree(preorder, inorder, postorder, length): 
    if length == 0:  
        return 1

    if length == 1:  
        return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0])
    idx = -1
      
    for i in range(length): 
        if inorder[i] == preorder[0]: 
            idx = i 
            break
    if idx == -1: 
        return 0
    ret1 = checktree(preorder[1:], inorder, postorder, idx)    
    ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:],  
                           postorder[idx:], length-idx-1)
    return (ret1 and ret2) 

if __name__ == "__main__": 
    import sys
    sys.setrecursionlimit(15000)
    _ , preorder , postorder , inorder = [ x.split() for x in sys.stdin.readlines()]
    len1 = len(inorder) 
    len2 = len(preorder) 
    len3 = len(postorder) 
  
    if (len1 == len2) and (len2 == len3): 
        correct = checktree(preorder, inorder,  postorder, len1) 
        if (correct):  
            print("yes")  
        else:  
            print("no") 
    else: 
        print("no")