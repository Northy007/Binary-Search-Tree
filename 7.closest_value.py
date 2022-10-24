class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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

    def closestValue(self, root, value):
        k = None
        queue = Queue()
        t = self.root
        queue.enQueue(t)
        while not queue.isEmpty():
            n = queue.deQueue()
            if k == None :
                k = n.data
            else :
                if abs(value - n.data) < abs(value - k):
                    k = n.data

            if n.left != None :
                queue.enQueue(n.left)
            if n.right != None :
                queue.enQueue(n.right)
        return k

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
inp[0] = inp[0].split()
for i in inp[0]:
    T.insert(int(i))
    T.printTree(T.root)
    print("--------------------------------------------------")
print("Closest value of {0} : {1}".format(int(inp[1]),T.closestValue(T.root,int(inp[1]))))