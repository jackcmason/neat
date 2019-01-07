class Connection:
    def __init__(self, inNode, outNode, weight, enabled, innov):
        self.inNode = inNode
        self.outNode = outNode
        self.weight = weight
        self.enabled = enabled
        #innovation number
        self.innov = innov
