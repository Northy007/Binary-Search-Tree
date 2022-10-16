class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        p = Node(data)
        if self.root == None :
            self.root = p
        else :
            t = self.root
            while t != None:
                if p.data < t.data:
                    if t.left == None :
                        t.left = p
                        break
                    else :
                        t = t.left
                elif p.data >= t.data:
                    if t.right == None:
                        t.right = p
                        break
                    else :
                        t = t.right

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
root = T.root
T.printTree(root)