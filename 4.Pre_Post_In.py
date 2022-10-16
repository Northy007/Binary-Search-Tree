class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    class Queue :
        def __init__(self, items = None) :
            if items == None or items == [] :
                self.items = []
            else :
                self.items = items

        def enQueue(self, i) :
            self.items.append(i) #insert ท้าย list

        def deQueue(self) :
            return self.items.pop(0) #pop ตัวหน้าสุดของ list

        def insert(self,i) :
            self.items.insert(0,i)

        def isEmpty(self) :
            return self.items == []

        def size(self) :
            return len(self.items)

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
    def Max(self):
        t = self.root
        while t.right != None:
            t = t.right
        return t.data

    def Min(self):
        t = self.root
        while t.left != None:
            t = t.left
        return t.data


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def BreadtFirst(self,root): #Level-Order
        queue = self.Queue()
        queue.enQueue(root)
        while not queue.isEmpty():
            n = queue.deQueue()
            print(n, end = " ")
            if n.left != None :
                queue.enQueue(n.left)
            if n.right != None :
                queue.enQueue(n.right)
    ##Depth-First Order
    def inOrder(self,root):
        if root != None :
            self.inOrder(root.left)
            print(root.data , end = " ")
            self.inOrder(root.right)

    def preOrder(self,root):
        if root != None :
            print(root.data, end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root != None :
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end = " ")

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
root = T.root
print("Preorder : ",end = ""); T.preOrder(root)
print()
print("Inorder : ",end = ""); T.inOrder(root)
print()
print("Postorder : ",end = ""); T.postOrder(root)
print()
print("Breadth : ",end = ""); T.BreadtFirst(root)

