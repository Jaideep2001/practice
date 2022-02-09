import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue1=[]
        queue1.append(root)
        result=""
        while len(queue1)!=0:
            result=result+str(queue1[0].data)+" "
            if queue1[0].left is not None:
                queue1.append(queue1[0].left)
            if queue1[0].right is not None:
                queue1.append(queue1[0].right)
            queue1.pop(0)
        print(result[:-1])

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
