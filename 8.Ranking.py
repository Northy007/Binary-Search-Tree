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
        self.rank = 0

    def insert(self, data):
        # Code Here
        if self.root == None :
            self.root = Node(data)
        else :
            root = self.root
            while root != None:
                if data < root.data:
                    if root.left == None :
                        root.left = Node(data)
                        break
                    root = root.left
                elif data >= root.data:
                    if root.right == None:
                        root.right = Node(data)
                        break
                    root = root.right
    
    def inOrder(self,root,k):
        if root != None :
            self.inOrder(root.left,k)
            if k >= root.data :
                self.rank += 1
            self.inOrder(root.right,k)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

tree = BST()
inp = input('Enter Input : ').split('/')
inp[0] = inp[0].split()
for i in inp[0]:
    tree.insert(int(i))
root = tree.root
tree.printTree(root)
print("--------------------------------------------------")
tree.inOrder(root,int(inp[1]))
print("Rank of {0} : {1}".format(int(inp[1]),tree.rank))