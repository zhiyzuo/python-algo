class Edge:
# {{{ Edge Class
    edge_id = 0
    def __init__(self, source, target, weight=1):
    # both source and target are Node objects
        self.source = source
        self.target = target
        if type(weight) == int:
            self.weight = weight
        else:
            self.weight = 1 # default
            print "Please enter an integer for weight! (Now set to default value 1)"
            print "Use setWeight method to reset the weight"

        self.id = Edge.edge_id
        Edge.edge_id = Edge.edge_id + 1

    def __eq__(self, edge):
        if self.source == edge.source and self.target == edge.target and self.weight == edge.weight:
            return True
        else:
            return False

    def __hash__(self):
        return self.id

    def __str__(self):
        return '({}, {}, {})'.format(self.source, self.target, self.getWeight())

    def __repr__(self):
        return self.__str__()

    def get_id(self):
        return self.id

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        if type(weight) == int:
            self.weight = weight
        else:
            print "Please enter an integer for weight! (Now set to default value 1)"
            self.weight = 1 # default
    
    def reverse(self):
        source = self.source
        target = self.target
        weight = self.weight
        return Edge(target, source, weight)
# }}}
