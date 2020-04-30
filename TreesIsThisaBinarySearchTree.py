""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
results = []
time = 1
def checkBST(root):
#     in order traversal
    if time == 1:
        onetime = root.data
        time = 0;

    def getRightChild(root):
        return root.right

    def getLeftChild(root):
        return root.left
    
    def getRootVal(root):
        return root.data

    if root:
        checkBST(getLeftChild(root))
        results.append(getRootVal(root))
        checkBST(getRightChild(root))
    
    if root.data 
    return results


