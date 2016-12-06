#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 03:08:34 2016

@author: jpdjere
"""
import graphs, shortestPath

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + " (" + str(self.getWeight())+")"