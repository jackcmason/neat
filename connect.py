class Connection:
    def __init__(self, inNode, outNode, weight, enabled, innov):
        self.inNode = inNode
        self.outNode = outNode
        self.weight = weight
        self.enabled = enabled
        #innovation number
        self.innov = innov

    def __str__(self):
        status = 'ENABLED' if self.enabled else 'DISABLED'
        return "Connection " + str(self.innov) + " with weight " + str(self.weight) + " is " + status + "\nconnects Node " + str(self.inNode.number) + " to Node " + str(self.outNode.number)
