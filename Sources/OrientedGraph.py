class OrientedGraph(object):
    """The class that implements an OrientedGraph.
    """

    def __init__(self,name="", filename=None):
        """ initialize an oriented Graph.
            The graph consists in a collection of arcs.
            the collection is a dictionnary.
            The key is a vertex (origin)
            the value is the list of vertex (target) that are connected to origin,
            so that origin -> target is an arc of the graph.
            """
        self.arcs = {}
        self.name = name

    def addVertex(self,n):
        """Add a vertex to the graph.
            The resulting vertex is not connected to any other node of the Graph.
            If the vertex already belongs to the graph, a message is written but nothing
            is done.
        """

        if n in self.arcs.keys():
            print ("vertex ",str(n), "is already in the graph")
        else :
            self.arcs[n]=[]


    def addArc(self,origin, target):
        """Add an arc to the Graph.
            If any vertex of the new arc does not belong to the Graph,
            they are added to the Graph.
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
        """
        if v in self.arcs.keys():
            return self.arcs[v]
        else :
            print ("This vertex does not belong to the Graph")
            return []

    def getPrevious(self, v):
        """Get the list of vertex that have v as a direct neighbor
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

    def toDot(self, filename = None):
        """ Produce a .dot output, as in the graphviz Library.
            If a filename is given, the method will save the produced string in
            a file. If not, it will be printed.
        """
        dotString = ""
        dotString+="digraph "+str(self.name) +" {\n"
        for origin in self.arcs.keys():
            ### if the node as arcs starting from it, print them.
            if self.arcs[origin]:
                ### if the node as arcs starting from it, print them.
                for target in self.arcs[origin]:
                    dotString+="\t"+str(origin) + " -> " + str(target) + ";\n"
            else :
                ### if the node is isolated, just note the node
                dotString+="\t"+str(origin)+";\n"

        dotString +="}"

        if filename == None :
            print (dotString)
        else :
            f = open(filename,"w+")
            f.write(dotString)
            f.close()

    def runBreadthFirst(self, start):
        toDo = [start]
        alreadyDone = []
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
            alreadyDone.append(current)

        return previous

    def getPath(self,start, end,previous):
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
        for n in path :
            print(n, end=" ")
