#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 23:35:38 2016

@author: jpdjere
"""

from graphs import Node, Edge, Digraph, Graph

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    
g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('BCA'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('ABC')))

print(g)