class DirectedGraph(object):
    """The class that implements a directed Graph.

    It's also the base class of all other Graphs.

    :param name: a graph optionnaly has a name. It is only used by
        :py:meth:`GraphLib.DirectedGraph.DirectedGraph.toDot`.
    """

    def __init__(self,name=""):
        """ initialize a directed Graph.
            The graph consists in a collection of arcs.
            the collection is a dictionnary.
            The key is a vertex (origin)
            the value is the list of vertices (target) that are connected to origin,
            so that origin -> target is an arc of the graph.
            """
        self.arcs = {}
        self.name = name

    def addVertex(self,v):
        """Add a vertex to the graph.
            The resulting vertex is not connected to any other node of the Graph.
            If the vertex already belongs to the graph, a message is written but nothing
            is done.
        """

        if v in self.arcs.keys():
            print ("vertex ",str(v), "is already in the graph")
        else :
            self.arcs[v]=[]


    def addArc(self,origin, target):
        """Add an arc to the Graph.
            If a vertex of the new arc does not belong to the Graph,
            it is added to the Graph.
            If the arc already belong to the graph, a message is written but nothing
            is done.
        """
        if not origin in self.arcs.keys():
            self.addVertex(origin)

        if not target in self.arcs.keys():
            self.addVertex(target)

        if origin in self.arcs[origin] :
            print ("this arc already belongs to the graph")
        else :
            self.arcs[origin].append(target)

    def getNeighbors(self, v):
        """Get the list of direct neighbors from vertex v

            :return: the list of vertices directly accessible from v
        """
        if v in self.arcs.keys():
            return self.arcs[v]
        else :
            print ("This vertex does not belong to the Graph")
            return []

    def getPrevious(self, v):
        """Get the list of vertices that have v as a direct neighbor

            :return: the list of vertices that give direct access to v

            .. warning:
                This is time consuming ans not at all optimized in the current
                implementation. use only in small graphs.
        """
        prev = []
        if v in self.arcs.keys():

            for orig in self.arcs.keys():
                if v in self.arcs[orig]:
                    prev.append(orig)
            return prev
        else :
            print ("This vertex does not belong to the Graph")
            return prev

    def _arcToDotString(self, origin, target):
        """An internal function to produce the string corresponding to an arc in a .dot file in the
            context of this type of graph.

            for directed graphs it takes the form : "origin -> target ;"
        """
        return "\t"+str(origin) + " -> " + str(target) + ";\n"



    def _toDotString(self):
        """ An internal function to produce the string corresponding to a .dot
            output, as in the graphviz Library.
        """
        dotString = ""
        dotString+="digraph "+str(self.name) +" {\n"
        for origin in self.arcs.keys():
            if self.arcs[origin]:
                ### if the node as arcs starting from it, print them.
                for target in self.arcs[origin]:
                    dotString+=self._arcToDotString(origin, target)
            else :
                # if the node is not the end of an arc, print it isolated
                if self.getPrevious(origin) == []:
                    ### if the node is isolated, just note the node
                    dotString+="\t"+str(origin)+";\n"

        dotString +="}"

        return dotString


    def toDot(self, filename = None):
        """ Produce a .dot output, as in the graphviz Library.
            If a filename is given, the method will save the produced string in
            a file. If not, it will be printed.
        """
        dotString = self._toDotString()
        if filename == None :
            print (dotString)
        else :
            f = open(filename,"w+")
            f.write(dotString)
            f.close()

    def runBreadthFirst(self, start):
        """ The BreadthFirstSearch Algorithm :
            It will make a search of all accessible vertices, starting at vertex
            *start*, following the Breadth First Search algorithm.

            :returns: previous : a dictionnary that contains all recorded paths.
                See :py:meth:`GraphLib.DirectedGraph.DirectedGraph.getPath`
                for a good description of this dictionary and its usage.
        """

        toDo = [start]
        # in BreadthFirstSearch algorithm, toDo is a FIFO.
        # beginning of the queue is at index 0 of the list.
        # new elements are put at the end of the list

        alreadyDone = set() # a HashSet...
        previous ={}

        while toDo :
            current=toDo[0]
            #print ("processing", str(current))

            for s in self.getNeighbors(current) :
                #print (s)
                if (not s in toDo) and (not s in alreadyDone):
                    previous[s]=current
                    toDo.append(s)

            toDo.remove(current)
            alreadyDone.add(current)

        return previous

    def getPath(self,start, end,previous):
        """ Get the succession of vertices on the path from vertex *start*
            to vertex *end*. Paths are stored in *previous*.

            :param start: the starting point of the path.
            :param end: the ending point of the path.
            :param previous: a way to store paths. It should be obtained by a
                search in the graph such as
                :py:meth:`GraphLib.DirectedGraph.DirectedGraph.runBreadthFirst`
                before this method is called. see below for more information of
                this structure

            :returns: a list of vertices found along the path from *start* to *end*

            Structure of the previous parameter :

                Most graph search returns a collection of recorded path from a certain
                vertex *start* to all accessible vertices.
                These recorded paths can be implemented as a dictionnary called *previous*
                *previous* is constructed as follows :

                - Each vertex *k* accessible from *start* is a key in the dictionnary.

                - The value *v* associated to *k* is the vertex from which one
                  should arrive to reach *k* on the path from *start* to *k*

                  Hence, one can retrieve a path from *start* to any vertex *end* accessible
                  by going backward in *previous* from *end* to its previous vertex and iterate
                  until *start* is found.


        """
        #print (previous)
        path = [end]
        current = end
        while not current == start :
            #print (current)
            prev = previous[current]
            path.insert(0,prev)
            current = prev

        return path

    def printPath(self,path):
        """ A path is a list of vertices.
        This function simply print every vertex in the path.

        No verification is made that the list of vertices is really a path in
        the graph (the vertices should be successive neighbors).
        """

        for n in path :
            print(n, end=" ")
        print("")
