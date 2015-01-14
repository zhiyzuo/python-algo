class Node:
# {{{ Node Class
    nodeID = 0
    def __init__(self, name):
        self.name = name
        self.id = Node.nodeID
        Node.nodeID = Node.nodeID + 1

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def copy(self):
        return Node(self.name)

    def __str__(self):
        return '<Node: id {} name {}>'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()
# }}}

class Edge:
# {{{ Edge Class
    EdgeID = 0

    def __init__(self, source, target, weight=1):
    # both source and target are Node objects
        self.source = source
        self.target = target
        if type(weight) == int:
            self.weight = weight
        else:
            self.weight = 1 # default
            print "Please enter an integer for weight! (Now set to default value 1)"

        self.id = Edge.EdgeID
        Edge.EdgeID = Edge.EdgeID + 1

    def getID(self):
        return self.id

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

    def getWeight(self):
        return self.weight

    def modifyWeight(self, weight):
        if type(weight) == int:
            self.weight = weight
        else:
            self.weight = 1 # default
            print "Please enter an integer for weight! (Now set to default value 1)"
    
    def reverse(self):
        source = self.source
        target = self.target
        weight = self.weight
        return Edge(target, source, weight)

    def __str__(self):
        return '<Edge id {} ({} -> {}) with weight {}>'.format(self.id, self.source.getName(), self.target.getName(), self.getWeight())

    def __repr__(self):
        return self.__str__()
# }}}

# undirected graph
class Graph:
# {{{ Graph Class

    GraphID = 0
    def __init__(self, nodes=[], edges=[]):
    # nodes: list of Node objects;
    # edges: list of Edge objects;

        if type(nodes) == list:
            self.nodes = nodes
        else:
            self.nodes = [nodes]

        if type(edges) == list:
            self.edges = edges
            reversedEdges = []
            for edge in self.edges:
                reversedEdge = edge.reverse()
                reversedEdges.append(reversedEdge)
            self.edges.extend(reversedEdges)

        else:
            self.edges = [edges, edges.reverse()]

        self.adjList = {}
        for edge in self.edges:
            source = edge.getSource()
            target = edge.getTarget()
            weight = edge.getWeight()
            if source in self.nodes and target in self.nodes:
                # no directions: add twice
                if source in self.adjList:
                    self.adjList[source].append((target, weight))
                else:
                    self.adjList[source] = [(target, weight)]
            else:
                print "source or target node is not eligible!"

        self.id = Graph.GraphID
        Graph.GraphID = Graph.GraphID + 1

    def getID(self):
        return self.id

    def getAdjList(self):
        return self.adjList

    def getNodes(self):
        return self.nodes

    def hasNode(self, node):
        return node in self.nodes

    def addNode(self, node):
        self.nodes.append(node)

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)

    def removeNode(self, node):
        if self.hasNode(node):
            self.nodes.remove(node)
        else:
            print "{} is not in this graph!".format(node)

    def removeNodes(self, nodes):
        for node in nodes:
            self.removeNode(node)

    def getEdges(self):
        return self.edges

    def hasEdge(self, edge):
        return edge in self.edges

    def addEdge(self, edge):
        source = edge.getSource()
        target = edge.getTarget()
        weight = edge.getWeight()
        if source in self.nodes and target in self.nodes:
            # no directions: add twice
            if source in self.adjList:
                self.adjList[source].append((target, weight))
            else:
                self.adjList[source] = [(target, weight)]

            if target in self.adjList:
                self.adjList[target].append((source, weight))
            else:
                self.adjList[target] = [(source, weight)]
        else:
            print "source or target node is not eligible!"

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge)

    def removeEdge(self, edge):
        if self.hasEdge(edge):
            self.edges.remove(edge)
            del self.adjList[edge.getSource()]
            del self.adjList[edge.getTarget()]
        else:
            print "{} is not in this graph!".format(edge)

    def removeEdges(self, edges):
        for edge in edges:
            self.removeEdge(edge)

    def __str__(self):
        string = '\nGraph id {} with\nnodes: {}\nedges:  '.format(self.id, self.nodes)
        for edge in self.edges:
            string += edge.__repr__() + '\n\t'  
        return string

    def __repr__(self):
        return self.__str__()
# }}}

class DiGraph(Graph):
# {{{ Directed Graph Class

    DiGraphID = 0

    def __init__(self, nodes=[], edges=[]):
    # nodes: list of Node objects;
    # edges: list of Edge objects;

        if type(nodes) == list:
            self.nodes = nodes
        else:
            self.nodes = [nodes]

        if type(edges) == list:
            self.edges = edges
        else:
            self.edges = [edges]

        self.adjList = {}
        for edge in self.edges:
            source = edge.getSource()
            target = edge.getTarget()
            weight = edge.getWeight()
            if source in self.nodes and target in self.nodes:
                # with directions: add once
                if source in self.adjList:
                    self.adjList[source].append((target, weight))
                else:
                    self.adjList[source] = [(target, weight)]
            else:
                print "source or target node is not eligible!"

        self.id = DiGraph.DiGraphID
        DiGraph.DiGraphID = DiGraph.DiGraphID + 1

    def __str__(self):
        string = '\nDirected Graph id {} with\nnodes: {}\nedges:  '.format(self.id, self.nodes)
        for edge in self.edges:
            string += edge.__repr__() + '\n\t'  
        return string

    def __repr__(self):
        return self.__str__()
# }}}
