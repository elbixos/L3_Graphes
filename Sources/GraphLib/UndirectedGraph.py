import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

import GraphLib.DirectedGraph

class UndirectedGraph(GraphLib.DirectedGraph.DirectedGraph):
    """The class that implements an undirected Graph.
    """

    def __init__(self,name="", filename=None):
        """ initialize an undirected Graph.
        It is basically a directed Graph with symetrical arcs.
        """
        GraphLib.DirectedGraph.DirectedGraph.__init__(self, name)

    def addArc(self,origin, target):
        """Add an undirected arc to the Graph.
            If a vertex of the new arc does not belong to the Graph,
            it is added to the Graph.
            If the arc already belong to the graph, a message is written but nothing
            is done.
        """
        GraphLib.DirectedGraph.DirectedGraph.addArc(self, origin, target)
        GraphLib.DirectedGraph.DirectedGraph.addArc(self, target, origin)
