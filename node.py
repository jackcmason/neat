class Node:
    def __init__(self, number, layer, nodeType):
        self.number = number
        self.layer = layer
        self.nodeType = nodeType

    def __str__(self):
        return "Node " + str(self.number) + " is " + self.nodeType + " on layer " + str(self.layer)
