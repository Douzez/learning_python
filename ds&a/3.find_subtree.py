"""
Given 2 binary trees t and s, find:
    * If s has an equal subtree in t, where the structure and the values are the same.
    * Return true if it exists, otherwise return false.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"(Value: {self.value} left: {self.left} right: {self.right})"


def find_subtree(t, s):
    # Fill this in
    # transform the tree into a string by using preorder traversal
    # Preorder traversal is print yourself before you print your children.
    def preorder_traversal(node):
        if node == None:
            return ''

        return str(node.value) + str(preorder_traversal(node.left)) + str(preorder_traversal(node.right))

    ts = preorder_traversal(t)
    print('T: ' + ts)
    ss = preorder_traversal(s)
    print('S: ' + ss)
    return ss in ts

tr = Node(5, Node(2), Node(3))
tl = Node(6, Node(7), Node(9))
t = Node(4, tl, tr)

s = Node(6, Node(7), Node(9))

print(find_subtree(t, s))

"""
   Tree t             Tree s
     4                  6
   /   \               / \
  6     5             7   9
 / \   / \
7   9 2   3

   Tree t             Tree s
     4                  6
   /   \               / \
  6     5             7   9
   \   / \
    9 2   3
"""

tr = Node(5, Node(2), Node(3))
tl = Node(6, Node(9))
t = Node(4, tl, tr)

s = Node(6, Node(7), Node(9))

print(find_subtree(t, s))
