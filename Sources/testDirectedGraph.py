
import GraphLib.DirectedGraph

def myMainDirected():
    g = GraphLib.DirectedGraph.DirectedGraph(name="myKickAssGraph")

    g.addArc("A", "B")
    g.addArc("B", "C")
    g.addArc("A", "C")
    g.addArc("B", "D")

    g.addVertex("X")
    g.addVertex("Y")

    g.toDot()

    g.toDot("bidon.dot")

    prev = g.runBreadthFirst("A")

    chemin = g.getPath("A","D",prev)

    g.printPath(chemin)



if __name__ == '__main__':
    myMainDirected()
