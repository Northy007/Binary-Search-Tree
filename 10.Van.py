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
    
    # def Book(self,num): #Level-Order
    #     queue = Queue()
    #     stack = Stack()
    #     queue.enQueue(self.root)
    #     while not queue.isEmpty():
    #         n = queue.deQueue()
    #         stack.push(n)
    #         stack.peek().day = num
    #         if stack.peek().left != None :
    #             queue.enQueue(n.left)   
    #         if stack.peek().right != None :
    #             queue.enQueue(n.right)
    #     return 
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    # def inOrder(self,root):
    #     if root != None :
    #         self.inOrder(root.left)
    #         if root.day != 0:
    #             root.day -= 1
    #         self.inOrder(root.right)


    

tree = BST()
inp = input('Enter Input : ').split('/')
Van = inp[0]
Custumer = inp[1].split()
# for member in range(1,int(Van) + 1):
#     tree.insert(int(member))
# n = 1
# for day in  Custumer:
#     tree.insert(int(day))
    
# root = tree.root
# tree.printTree(root)    
