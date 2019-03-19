import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

from GraphLib.DirectedGraph import DirectedGraph

class UndirectedGraph(DirectedGraph):
    """The class that implements an undirected Graph.
    """

    def __init__(self,name="", filename=None):
        """ initialize an undirected Graph.
        It is basically a directed Graph with symetrical arcs.
        """
        DirectedGraph.__init__(self, name)

    def addArc(self,origin, target):
        """Add an undirected arc to the Graph.
            If a vertex of the new arc does not belong to the Graph,
            it is added to the Graph.
            If the arc already belong to the graph, a message is written but nothing
            is done.
        """
        DirectedGraph.addArc(self, origin, target)
        DirectedGraph.addArc(self, target, origin)
