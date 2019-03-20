import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

import GraphLib.DirectedGraph

class WeightedDirectedGraph(GraphLib.DirectedGraph.DirectedGraph):
    """The class that implements an weighted directed Graph.

    It is basically a directed Graph where arcs have weights
    """

    def __init__(self,name=""):
        """ initialize a weighted directed Graph.
        It is basically a directed Graph where arcs have weights (float)

        weights are coded as a dictionnary :
            - the key is a tuple of vertex (origin, target)
            - the value is the weight of the arc from origin to target
        """
        GraphLib.DirectedGraph.DirectedGraph.__init__(self, name)
        self.weights = {}

    def addArc(self,origin, target, weight = 1.0):
        """Add a weighted arc to the Graph.

            If a vertex of the new arc does not belong to the Graph,
            it is added to the Graph.
            If the arc already belong to the graph, a message is written but nothing
            is done.
        """
        GraphLib.DirectedGraph.DirectedGraph.addArc(self, origin, target)
        self.weights[(origin,target)] = float(weight)

    def getArcWeight (self, origin, target):
        """get the weight of an arc in the graph

            If the arc does not belong to the graph, a key Exception is raised
        """
        return self.weights[(origin,target)]

    def _arcToDotString(self, origin, target):
        """ An intern function to produce the string corresponding to a an arc
            in a .dot file in the context of this type of graph.

            for weighted directed graphs it takes the form :
                "origin -> target [ label = "weight" ] ;"
        """
        return "\t"+str(origin) + " -> " + str(target) + "[ label = \"" \
            +str(self.getArcWeight(origin, target)) + "\"];\n"

    def _getMinDistance(self,toDo, distances):
        """ An intern function for the Diskstra Algorithm :
            it looks in the toDo list which vertex is the closest to *start*

            :param toDo: the list of vertices to examine
            :param distances: a dictionnary of distances (usually to *start* vertex)
                    - the key is a vertex *v*
                    - the value is the distance from *start* to *v*

            :return: minVertex: the vertex in toDo with the smallest distance.
        """
        minVertex = toDo[0]
        minDist = distances[minVertex]
        for v in toDo:
            if distances[v] < minDist:
                minDist = distances[v]
                minVertex = v
        return minVertex


    def runDijkstra(self, start):
        """ The Diskstra Algorithm :
            It will make a search of all accessible vertices, starting at vertex
            *start* and compute the smallest path to all of them, taking the weights
            of arcs into account.

            :param start: the starting vertex of the search.

            :return: (previous, distances)
                - previous : a dictionnary that contains all recorded paths.
                Each vertex accessible *k* is a key in the dictionnary. The value *v*
                associated to *k* is the vertex from which one should arrive to reach *k*
                - distances : a dictionnary of the distance from *start* to every
                accessible vertex in the graph.

                    - the key is a vertex *v*
                    - the value is the distance from *start* to *v*

            Hence, one can retrieve a path from *start* to any vertex *a* accessible
            by going backward in *previous* from *a* to its previous vertex and iterate
            until *start* is found. This is done by the getPath method

            .. warning::
                The search for a current vertex to explore is not at all optimal
                in the current implementation. A priority queue should be used instead.

        """
        toDo = [start]
        alreadyDone = []
        previous ={}
        distances = {start : 0.0}

        while toDo :
            current=self._getMinDistance(toDo, distances)
            #print ("processing", str(current))

            for s in self.getNeighbors(current) :
                #print (s)
                if (not s in alreadyDone):
                    # compute the distance of the new path
                    newDist = distances[current]+self.getArcWeight(current,s)
                    ## did we see it before ?
                    if not s in distances.keys():
                        previous[s]=current
                        distances[s]= newDist
                        toDo.append(s)
                    else :
                        oldDist = distances[s]
                        if newDist < oldDist :
                            previous[s]=current
                            distances[s]= newDist

            toDo.remove(current)
            alreadyDone.append(current)

        return previous, distances
