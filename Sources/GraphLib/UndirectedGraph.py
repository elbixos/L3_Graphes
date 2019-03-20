import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

import GraphLib.DirectedGraph

class UndirectedGraph(GraphLib.DirectedGraph.DirectedGraph):
    """The class that implements an undirected Graph.

    It is basically a directed Graph with symetrical arcs.
    """

    def __init__(self,name=""):
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

    def _arcToDotString(self, origin, target):
        """ An intern function to produce the string corresponding to a an arc in a .dot file in the
            context of this type of graph.

            for undirected graphs it takes the form : "origin -- target ;"
        """
        return "\t"+str(origin) + " -- " + str(target) + ";\n"


    def toDotString(self, filename = None):
        """ Produce the string corresponding to a .dot output, as in the graphviz Library.

        It overrides the method of DirectedGraph since it's quite different.
        """
        # We do not want to double each connection.
        # Hence, we keep track of Vertex done as origin, since we will
        # not add a arc if they are target of an arc already considered.
        doneVertices = []

        dotString = ""
        dotString+="graph "+str(self.name) +" {\n"
        for origin in self.arcs.keys():
            doneVertices.append(origin)
            if self.arcs[origin]:
                ### if the node as arcs starting from it, print them.
                for target in self.arcs[origin]:
                    ##
                    if not target in doneVertices :
                        dotString+=self._arcToDotString(origin, target)
            else :
                # if the node is not the end of an arc, print it isolated
                if self.getPrevious(origin) == []:
                    ### if the node is isolated, just note the node
                    dotString+="\t"+str(origin)+";\n"

        dotString +="}"

        return dotString
