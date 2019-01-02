class BinaryTree():

    def __init__(self,rootid,value):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = value

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.value = value
    def getNodeValue(self):
        return self.value
    def getNodeId(self):
        return self.rootid

    def insertRight(self,newNode,value):
        if self.right == None:
            self.right = BinaryTree(newNode,value)
        else:
            tree = BinaryTree(newNode,value)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode,value):
        if self.left == None:
            self.left = BinaryTree(newNode,value)
        else:
            tree = BinaryTree(newNode,value)
            tree.left = self.left
            self.left = tree


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())

#Max1
max1 = BinaryTree("l1_0",0)
max1.insertLeft("l2_1", 0)
max1.insertRight("l2_2", 0)

#Min1
min1 = max1.getLeftChild()
min1.insertLeft("l3_3", 0)
min1.insertRight("l3_4", 0)

#Min2
min2 = max1.getRightChild()
min2.insertLeft("l3_5", 0)
min2.insertRight("l3_6", 0)

#Max2
max2 = min1.getLeftChild()
max2.insertLeft("l4_7", 0)
max2.insertRight("l4_8", 0)

#Max3
max3 = min1.getRightChild()
max3.insertLeft("l4_9", 0)
max3.insertRight("l4_10", 0)

#Max4
max4 = min2.getLeftChild()
max4.insertLeft("l4_11", 0)
max4.insertRight("l4_12", 0)

#Max5
max5 = min2.getRightChild()
max5.insertLeft("l4_13", 0)
max5.insertRight("l4_14", 0)

#Min3
min3 = max2.getLeftChild()
min3.insertLeft("l5_15", 3)
min3.insertRight("l5_16", 10)

#Min4
min4 = max2.getRightChild()
min4.insertLeft("l5_17", 2)
min4.insertRight("l5_18", 9)

#Min5
min5 = max3.getLeftChild()
min5.insertLeft("l5_19", 10)
min5.insertRight("l5_20", 7)

#Min6
min6 = max3.getRightChild()
min6.insertLeft("l5_21", 5)
min6.insertRight("l5_22", 9)

#Min7
min7 = max4.getLeftChild()
min7.insertLeft("l5_23", 2)
min7.insertRight("l5_24", 5)

#Min8
min8 = max4.getRightChild()
min8.insertLeft("l5_25", 6)
min8.insertRight("l5_26", 4)

#Min9
min9 = max5.getLeftChild()
min9.insertLeft("l5_27", 2)
min9.insertRight("l5_28", 7)

#Min0
min0 = max5.getRightChild()
min0.insertLeft("l5_29", 9)
min0.insertRight("l5_30", 1)

path = list()

def max_value(state, a, b):
    v = 0
    children = [state.getLeftChild(), state.getRightChild()]
    for successor in children:
        v = max(v, value(successor, a, b))
        if v >= b:
            return v

        a = max(a, v)

    state.setNodeValue(v)
    return v

def min_value(state, a, b):
    v = 100
    children = [state.getLeftChild(), state.getRightChild()]
    for successor in children:
        v = min(v, value(successor, a, b))
        if v <= a:
            return v
        b = min(b, v)

    state.setNodeValue(v)
    return v

def value(state, a, b):
    if "l5" in state.getNodeId():
        return state.getNodeValue()

    if "l1" in state.getNodeId() or "l3" in state.getNodeId():
        return max_value(state, a, b)

    if "l2" in state.getNodeId() or "l4" in state.getNodeId():
        return min_value(state, a, b)

def get_path(output, state):
    global path
    path.append(state.getNodeId())
    if state.getLeftChild() != None:
        if state.getLeftChild().getNodeValue() is output:
            get_path(output, state.getLeftChild())

        else:
            get_path(output, state.getRightChild())

a = 0
b = 11  

print("Output value:")
output = value(max1, a, b)
print(output)
get_path(output, max1)
print("Output path: ")
print(path)