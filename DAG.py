from graph import *

class DAG:
    def __init__(self, nodes=[], edges=[]):
        if type(nodes) == list:
            self.nodes = nodes
        else:
            self.nodes = [nodes]

        # edge should be in form of tulpe (u, v, w)
        # (u, v) indicates from u -> v weighted by w
        if type(edges) == list:
            self.edges = edges
        else:
            self.edges = [edges]

        self.adjList = {}
        for node in self.nodes:
            self.adjList[node] = None
        for edge in self.edges:
            source = edge[0]
            target = edge[1]
            weight = edge[2]
            if source in self.nodes and target in self.nodes:
                self.adjList[source] = (target, weight)
            else:
                print "source or target node is not eligible!"

    def addNode(self, node):
        self.nodes.extend(node)

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)

    def addEdge(self, source, target, weight=1):
        if source in self.nodes and target in self.nodes:
            self.edges.append((source, target, weight))
            self.adjList[source] = (target, weight)
        else:
            print "source or target node is not eligible!"

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge)

    def removeNode(self, node):
        try:
            self.nodes.remove(node)
        except:
            print "{} is not in this dag!".format(node)

    def removeNodes(self, nodes):
        for node in nodes:
            self.removeNode(node)

    def removeEdge()
