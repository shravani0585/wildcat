# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:28:32 2019

@author: 
Student Name:				Student ID:
Shravani Gangi Reddy		999993962
Prathyusha Dasyam			999993818
Satish Lingam				999900097


"""

import sys

#from functools import total_ordering

import colorama
from colorama import Fore
from colorama import Back

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None


    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight


    def get_connections(self):
        return self.adjacent.keys()  


    def get_id(self):
        return self.id


    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


    def set_distance(self, dist):
        self.distance = dist


    def get_distance(self):
        return self.distance


    def set_previous(self, prev):
        self.previous = prev


    def set_visited(self):
        self.visited = True


    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.distance == other.distance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
        return NotImplemented
    def __hash__(self):
        return id(self)


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0


    def __iter__(self):
        return iter(self.vert_dict.values())


    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex


    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None


    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)


        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)


    def get_vertices(self):
        return self.vert_dict.keys()


    def set_previous(self, current):
        self.previous = current


    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return




import heapq


def dijkstra(Graph, start):
    print ("Dijkstra's shortest path")
    
    # Set the distance for the start node to zero 
    start.set_distance(0)


    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in Graph]
    heapq.heapify(unvisited_queue)


    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        currentnode = uv[1]
        currentnode.set_visited()


        #for next in v.adjacent:
        for next in currentnode.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = currentnode.get_distance() + currentnode.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(currentnode)
                print (Fore.BLUE + 'currentnode = %s nextnode = %s new_dist = %s' \
                        %(currentnode.get_id(), next.get_id(), next.get_distance()))
                
            else:
                print (Fore.RED + 'ignore : currentnode = %s nextnode = %s new_dist = %s' \
                        %(currentnode.get_id(), next.get_id(), next.get_distance()))
                


        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in Graph if not v.visited]
        heapq.heapify(unvisited_queue)
        
if __name__ == '__main__':

    # Adding vertex
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_vertex('g')
    g.add_vertex('h')
    g.add_vertex('i')
    g.add_vertex('j')
    g.add_vertex('k')
    g.add_vertex('l')
    g.add_vertex('m')
    g.add_vertex('n')
    g.add_vertex('o')
    g.add_vertex('p')
    g.add_vertex('q')
    g.add_vertex('r')
    g.add_vertex('s')
    g.add_vertex('t')


# Creating edges
    
    g.add_edge('a', 'b', 10)  
    g.add_edge('a', 'f', 13)
    g.add_edge('b', 'g', 7)
    g.add_edge('b', 'c', 17)
    g.add_edge('c', 'd', 7)
    g.add_edge('c', 'h', 3)
    g.add_edge('d', 'e', 14)
    g.add_edge('d', 'i', 9)
    g.add_edge('e', 'j', 13)
    g.add_edge('f', 'g', 6)  
    g.add_edge('f', 'k', 15)
    g.add_edge('g', 'h', 5)
    g.add_edge('g', 'l', 10)
    g.add_edge('h', 'i', 18)
    g.add_edge('h', 'm', 7)
    g.add_edge('i', 'j', 4)
    g.add_edge('i', 'n', 2)
    g.add_edge('j', 'o', 4)
    g.add_edge('k', 'l', 5)  
    g.add_edge('k', 'p', 17)
    g.add_edge('l', 'm', 8)
    g.add_edge('l', 'q', 13)
    g.add_edge('m', 'n', 7)
    g.add_edge('m', 'r', 9)
    g.add_edge('n', 'o', 20)
    g.add_edge('n', 's', 14)
    g.add_edge('o', 't', 7)
    g.add_edge('p', 'q', 14)  
    g.add_edge('q', 'r', 11)
    g.add_edge('r', 's', 9)
    g.add_edge('s', 't', 12)

# Print graph data that was created
    
    print ('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print (' %s , %s, %3d '  % ( vid, wid, v.get_weight(w)))

# Calling dijkstra function to calculate shortest path from Source A to T
            
    dijkstra(g, g.get_vertex('a')) 

# Setting the target
    target = g.get_vertex('t')
    
    # Save the path
    path = [target.get_id()]
    shortest(target, path)
    
   # printing the shortest path 
    print (Fore.GREEN + 'The shortest path : %s' %(path[::-1]))
    
'''
we have used system specific parameters and functions, and also imported the functools for
 total ordering.
The comparison operators (<, <=, >, >=, == and !=) can be overloaded by providing definition to
 __lt__, __hash_, __eq__ methods, these are used to compare distance between objects.


we represented the graph using vertex(each rows and columns represent a vertex in graph).
In this implementation we have created two classes graph g, which has the list of 
vertex and vertices and class vertex which uses dictionary in order to implement adjacent list.
Using add neighbour we addressed connection from one vertex to another.

we used hashable objects inorder to support custom comparisions and also used heap queue in order to
 represent a priority queue to push, pop and maintain the heap structure.
 
Algorithm steps:

1.Mark all unvisited vertices
2.Set the distance to zero for our initial node and to infinity for other nodes.
3.Select the unvisited node with the smallest distance, which makes it as current node.
4.Find unvisited neighbors for the current node and calculate their distances through the current node.
5.Compare the newly calculated distance to the assigned and save the smaller value.
6.Mark the current node as visited and remove it from the unvisited set.
7.Stop, if the destination node has been visited 
and calculates the shortest path.

'''
 


 

 
