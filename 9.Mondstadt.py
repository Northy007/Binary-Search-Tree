class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.number = None
    
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
        self.sum = 0
        self.size = 0

    def insert(self, data):
        # Code Here
        if self.root == None :
            self.root = Node(data)
            self.root.number = 0
        else :
            root = self.root
            while root != None:
                if data < root.data:
                    if root.left == None :
                        root.left = Node(data)
                        root.left.number = self.size
                        break
                    root = root.left
                elif data >= root.data:
                    if root.right == None:
                        root.right = Node(data)
                        root.right.number = self.size
                        break
                    root = root.right
        self.sum += data
        self.size += 1
    
    def Power(self,num): #Level-Order
        queue = Queue()
        root = self.root
        power = 0
        queue.enQueue(root)
        while not queue.isEmpty():
            n = queue.deQueue()
            if n.number == num:
                power = n.data
                break
            if n.left != None :
                queue.enQueue(n.left)
            if n.right != None :
                queue.enQueue(n.right)
        return power

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

tree = BST()
inp = input('Enter Input : ').split('/')
Favonius = inp[0].split()
compare_list = inp[1].split(",")
for member in Favonius:
    tree.insert(int(member))
root = tree.root
print(tree.sum)
for n in  compare_list:
    team1 = tree.Power(int(n[0])) + tree.Power(2*int(n[0]) + 1) + tree.Power(2*int(n[0]) + 2)
    team2 = tree.Power(int(n[2])) + tree.Power(2*int(n[2]) + 1) + tree.Power(2*int(n[2]) + 2)
    if team1>team2: print(n[0] +">" + n[2])
    if team1<team2: print(n[0] +"<" + n[2])
    if team1==team2: print(n[0] +"=" + n[2])
    
