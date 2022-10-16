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

    def BreadtFirst(self): #Level-Order
        queue = self.Queue()
        t = self.root
        queue.enQueue(t)
        while not queue.isEmpty():
            n = queue.deQueue()
            if n.left != None :
                queue.enQueue(n.left)
            if n.right != None :
                queue.enQueue(n.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, val):
        if self.root.data == val:
            print("Root")
        else :
            queue = self.Queue()
            t = self.root
            queue.enQueue(t)
            pos = None
            while not queue.isEmpty():
                n = queue.deQueue()
                if n.data == val :
                    pos = n
                    break
                if n.left != None :
                    queue.enQueue(n.left)
                if n.right != None :
                    queue.enQueue(n.right)
            if pos != None :
                if pos.left != None or pos.right != None :
                    print("Inner")
                else :
                    print("Leaf")
            else :
                print("Not exist")

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    T.insert(inp[i])
root = T.root
T.printTree(root)
T.checkpos(inp[0])