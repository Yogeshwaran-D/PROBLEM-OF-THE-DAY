class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions) :
        new_dict={}
        children=set()
        for parent,child,dis in descriptions:
            children.add(child)
            if parent not in new_dict:
                new_dict[parent]=TreeNode(parent)
            if child not in new_dict:
                new_dict[child]=TreeNode(child)
            if dis:
                new_dict[parent].left=new_dict[child]
            else:
                new_dict[parent].right=new_dict[child]
        for parent,child,dis in descriptions:
            if parent not in children :
                return new_dict[parent] 