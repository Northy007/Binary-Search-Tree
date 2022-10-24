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
        s = ''
        if self.root == None :
            self.root = p
            s = '*'
        else :
            t = self.root
            while t != None:
                if p.data < t.data:
                    if t.left == None :
                        t.left = p
                        s += "L*"
                        break
                    else :
                        t = t.left
                        s += "L"
                elif p.data >= t.data:
                    if t.right == None:
                        t.right = p
                        s += "R*"
                        break
                    else :
                        t = t.right
                        s += 'R'
        return s

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    print(T.insert(i))
# root = T.root
# T.printTree(root)