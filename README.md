we have used system specific parameters and functions, and also imported the functools for
 total ordering.
The comparison operators (<, <=, >, >=, == and !=) can be overloaded by providing definition to
 __lt__, __hash_, __eq__ methods, these are used to compare distance between objects.
Represented the graph using vertex(each rows and columns represent a vertex in graph).
In this implementation I have created two classes graph g, which has the list of 
vertex and vertices and class vertex which uses dictionary in order to implement adjacent list.
Using add neighbour I addressed connection from one vertex to another.
Used hashable objects inorder to support custom comparisions and also used heap queue in order to
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
