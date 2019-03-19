
import GraphLib.WeightedDirectedGraph

def myMainWeightedDirected():
    g = GraphLib.WeightedDirectedGraph.WeightedDirectedGraph(name="myKickAssGraph")

    g.addArc("A", "B")
    g.addArc("B", "C",3.0)
    g.addArc("A", "C",2.0)
    g.addArc("B", "D")

    g.addVertex("X")
    g.addVertex("Y")

    g.toDot()

    print (g.getArcWeight("A","B"))
    print (g.getArcWeight("A","C"))
    print (g.getArcWeight("B","C"))


    g.toDot("bidonWeighted.dot")

    prev = g.runBreadthFirst("A")

    chemin = g.getPath("A","D",prev)

    g.printPath(chemin)



if __name__ == '__main__':
    myMainWeightedDirected()
