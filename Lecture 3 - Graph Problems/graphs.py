# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
        
    def getName(self):
        return self.name
        
        
    def __str__(self):
        return self.getName()
        
        
class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
        
    def __str__(self):
        return self.src.getName() + ' --> ' + self.dest.getName()
        
    
class Digraph(object):
    """edges is a dict that maps each node to a list of its children"""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        
    def childreOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        return NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' -> ' + dest.getName() + '\n'
        return result[:-1] #omit final newline
        
class Graph(Digraph):
    
    def addEdge(self, edge):
        #Agrego el Edge primero como un Diagraph
        Digraph.addEdge(self, edge)
        #Agrego la reversa para transformarlo en un Graph bidireccional normal
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

#Build the Graph
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston','Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'LA'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('LA'), g.getNode('Boston')))
    return g

print(buildCityGraph(Graph))