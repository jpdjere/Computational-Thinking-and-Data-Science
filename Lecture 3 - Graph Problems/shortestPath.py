#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 00:07:48 2016

@author: jpdjere
"""

import graphs

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result
    
def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and End are nodes;
        path and shortest are lists of nodes
        Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print("Current DFS path:", printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print("Already visited", node)
    return shortest
    
def shortestPath(graph, start, end, toPrint=False):
    """Assumes a graph is a Digraph: start and end are nodes
    Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)
    
def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to ', destination, 'is ', printPath(sp))
    else:
        print('There is no path from ', source , 'to ', destination)

testSP('Boston', 'Phoenix')


def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath] #used to store all paths currently being explored
    if toPrint:
        print('Current BFS path: ', printPath(pathQueue))
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path: ', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            #As soon as it finds a paths where the lastNode is the end, it will
            #return it. That is so, because BFS is exploring the paths in node
            #order and it will surely be the shortest or one of the shortest.
            
            #if we want to minimize the sum of the weights of the edges, not the
            #number of edges, DFS can esasily be modified to do this.
            #But BFS cannot, since the shrotest weighted path may have more
            #than the minimum number of hops
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
    
    
    
def shortestPath(graph, start, end, toPrint=False):
    """Assumes a graph is a Digraph: start and end are nodes
    Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)    
    
testSP('Boston', 'Phoenix')   
    
    
#--------------------------------COPIR EXPLICACION DE ARRIBA DE BFS EN CUADERNO    
    
    
    
    
    
    
    
    
    