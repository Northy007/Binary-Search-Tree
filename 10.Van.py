class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.day = 0
    
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
        self.size = 0

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
        self.size += 1
    
    def Book(self,num): #Level-Order
        queue = Queue()
        root = self.root
        power = 0
        queue.enQueue(root)
        while not queue.isEmpty():
            n = queue.deQueue()
            if n.day == 0:
                n.day = num
                break
            n.day -= 1
            if n.left != None :
                queue.enQueue(n.left)
            if n.right != None :
                queue.enQueue(n.right)
        return n

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

tree = BST()
inp = input('Enter Input : ').split('/')
Van = inp[0]
Custumer = inp[1].split()
for member in range(1,int(Van) + 1):
    tree.insert(int(member))
root = tree.root
n = 1

for day in  Custumer:
    print("Customer {0} Booking Van {1} | {2} day(s)".format(n,tree.Book(int(day)),day))
    n += 1
