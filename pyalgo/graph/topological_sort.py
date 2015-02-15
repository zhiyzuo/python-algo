# -*- coding: utf-8 -*-
from data_structure import Stack

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
