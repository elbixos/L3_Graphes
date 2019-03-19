import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

import GraphLib.UndirectedGraph

class WeightedUndirectedGraph(GraphLib.UndirectedGraph.UndirectedGraph):
    """The class that implements an weighted undirected Graph.

    It is basically an undirected Graph where arcs have weights
    """

    def __init__(self,name="", filename=None):
        """ initialize a weighted undirected Graph.
        It is basically an undirected Graph where arcs have weights (float)

        weights are coded as a dictionnary :
            - the key is a tuple of vertex (origin, target)
            - the value is the weight of the arc from origin to target
        """
        GraphLib.UndirectedGraph.UndirectedGraph.__init__(self, name)
        self.weights = {}

    def addArc(self,origin, target, weight = 1.0):
        """Add a weighted arc to the Graph.

            If a vertex of the new arc does not belong to the Graph,
            it is added to the Graph.
            If the arc already belong to the graph, a message is written but nothing
            is done.
        """
        GraphLib.UndirectedGraph.UndirectedGraph.addArc(self, origin, target)
        self.weights[(origin,target)] = float(weight)

    def getArcWeight (self, origin, target):
        """get the weight of an arc in the graph

            If the arc does not belong to the graph, a key Exception is raised
        """
        return self.weights[(origin,target)]

    def arcToDotString(self, origin, target):
        """ Produce the string corresponding to a an arc in a .dot file in the
            context of this type of graph.

            for weighted undirected graphs it takes the form :
                "origin -- target [ label = "weight" ] ;"
        """
        return "\t"+str(origin) + " -- " + str(target) + "[ label = \"" \
            +str(self.getArcWeight(origin, target)) + "\"];\n"
