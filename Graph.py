class Node:
# {{{ Node Class
    nodeID = 0
    # records edges that are already created
    taken = []
    def __init__(self, name):
        if name not in Node.taken:
            self.name = name
            self.id = Node.nodeID
            Node.nodeID = Node.nodeID + 1
            Node.taken.append(name)
        else:
            print "{} has been taken!".format(name)

    def __eq__(self, node):
        if self.name == node.name:
            return True
        else:
            return False

    # make Node objects hashable
    # (Act as dict keys)
    def __hash__(self):
        return self.id

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def copy(self):
        return Node(self.name)

    def __str__(self):
        return 'Node {}'.format(self.name)

    def __repr__(self):
        return 'Node {}'.format(self.name)
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
            print "Use setWeight method to reset the weight"

        self.id = Edge.EdgeID
        Edge.EdgeID = Edge.EdgeID + 1


    def __eq__(self, edge):
        if self.source == edge.source and self.target == edge.target and self.weight == edge.weight:
            return True
        else:
            return False

    def __hash__(self):
        return self.id

    def getID(self):
        return self.id

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
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

    def __str__(self):
        return '({}, {}, {})'.format(self.source, self.target, self.getWeight())

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
            reverse = []
            # both directions are needed
            for edge in edges:
                reverse.append(edge.reverse())
            self.edges.extend(reverse)
        else:
            self.edges = [edges, edges.reverse()]
            # self.edges = [edges]

        self.type = 'undirected'
        self.id = Graph.GraphID
        Graph.GraphID = Graph.GraphID + 1

    def getID(self):
        return self.id

    def getType(self):
        return self.type

    def getNodes(self):
        return self.nodes

    def hasNode(self, node):
        return node in self.nodes

    def addNode(self, node):
        if self.hasNode(node):
            print "{} is already in the graph".format(node)
        else:
            self.nodes.append(node)

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)

    def removeNode(self, node):
        # also remove edges that include the node
        if self.hasNode(node):
            self.nodes.remove(node)
            remove = []
            for edge in self.edges:
                source = edge.getSource()
                target = edge.getTarget()
                if source == node or target == node:
                    remove.append(edge)
            for edge in remove:
                self.edges.remove(edge)

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
        if self.hasEdge(edge):
            print "{} is already in this graph".format(edge)
            return 
        source = edge.getSource()
        target = edge.getTarget()
        if source in self.nodes and target in self.nodes:
            self.edges.extend([edge, edge.reverse()])
        else:
            print "source or target node of this edge is not eligible!"

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge)

    def removeEdge(self, edge):
        reversedEdge = edge.reverse()
        if self.hasEdge(edge) and self.hasEdge(reversedEdge):
            self.edges.remove(edge)
            self.edges.remove(reversedEdge)
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

# directed graph
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

        self.type = 'directed'
        self.id = DiGraph.DiGraphID
        DiGraph.DiGraphID = DiGraph.DiGraphID + 1

    def getEdges(self):
        return self.edges

    def hasEdge(self, edge):
        return edge in self.edges

    def addEdge(self, edge):
        if self.hasEdge(edge):
            print "({}, {}) is already in this graph".format(edge.getSource().getName(), edge.getTarget().getName())
            return 
        source = edge.getSource()
        target = edge.getTarget()
        if source in self.nodes and target in self.nodes:
            self.edges.append(edge)
        else:
            print "source or target node of this edge is not eligible!"

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge)

    def removeEdge(self, edge):
        if self.hasEdge(edge):
            self.edges.remove(edge)
        else:
            print "{} is not in this graph!".format(edge)

    def removeEdges(self, edges):
        for edge in edges:
            self.removeEdge(edge)

    def __str__(self):
        string = '\nDiGraph ID {} with\nnodes: {}\nedges:  '.format(self.id, self.nodes)
        for edge in self.edges:
            string += edge.__repr__() + '\n\t'  
        return string

    def __repr__(self):
        return self.__str__()
# }}}

class AdjacencyList:
# {{{ Adjacency List Class
    def __init__(self, graph):
        self.adjList = {}
        for edge in graph.getEdges():
            source = edge.getSource()
            target = edge.getTarget()
            if source in self.adjList:
                self.adjList[source].append(target)
            else:
                self.adjList[source] = [target]
        for node in graph.getNodes():
            if node not in self.adjList:
                self.adjList[node] = []

    def __str__(self):
        string = 'Adjancency List\n'
        for node in self.adjList:
            string += str(node) + ': '
            if len(self.adjList[node]) > 0:
                for neighbour in self.adjList[node]:
                    string += str(neighbour) + '; '
            else:
                string += 'null'
            string += '\n'
        return string

    def __repr__(self):
        return self.__str__()

    def getAdjacencyList(self):
    # get the dictionary of representations
        return self.adjList
    

# }}} 

class AdjacencyMatrix:
# {{{ Adjacency Matrix Class
    def __init__(self, graph):

        nodes = graph.getNodes()
        self.nodesIndices = {}
        index = 0
        for node in nodes:
            self.nodesIndices[node] = index
            index = index + 1

        # Note: use list comprehension to create 2-dim list
        self.matrix = [ ([0] * index) for row in xrange(index) ]

        edges = graph.getEdges()
        for node in nodes:
            for edge in edges:
                source = edge.getSource()
                sourceIndex = self.nodesIndices[source]
                # put weight in (u, v) if there's an edge between u and v
                if source == node:
                    targetIndex = self.nodesIndices[edge.getTarget()]
                    print sourceIndex, targetIndex
                    self.matrix[sourceIndex][targetIndex] = edge.getWeight()
                    print self.matrix

    def __str__(self):
        string = '\t' * (len(self.nodesIndices)//2)
        string += 'Adjancency Matrix\n\n'
        for row in self.matrix:
            for entry in row:
                string += "\t" + str(entry)
            string += '\n'
        string += "\n-- Nodes' indices: {} --\n".format(self.nodesIndices)
        return string

    def __repr__(self):
        return self.__str__()

    def getNodesIndices(self):
        return self.nodesIndices

    def getMatrix(self):
        return self.matrix

# }}} 

# Algorithms for graphs
from DataStructure import *

def topologicalSort(dag):
    ''' Return a list containing a linear order
        of the given directed acyclic graph;
        Input should be an adjacency list;
    '''
    adjacencyList = dag.getAdjacencyList()
    linearOrder = []
    nextNodes = Stack()

    indegree = {}
    for node in adjacencyList:
        for neighbour in adjacencyList[node]:
            if neighbour in indegree:
                indegree[neighbour] += 1
            else:
                indegree[neighbour] = 1
    
    for node in adjacencyList:
        if node not in indegree:
            indegree[node] = 0
            nextNodes.push(node)

    while nextNodes.getSize() > 0:
        nextNode = nextNodes.pop()
        linearOrder.append(nextNode)
        for neighbour in adjacencyList[nextNode]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                nextNodes.push(neighbour)

    return linearOrder
