
import GraphLib.WeightedUndirectedGraph

def myMainWeightedUndirected():
    g = GraphLib.WeightedUndirectedGraph.WeightedUndirectedGraph(name="myKickAssGraph")

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


    g.toDot("bidonWeightedUndirected.dot")

    start ="A"
    end = "D"
    print("\nBreadthFirstSearch from ",start)
    prev = g.runBreadthFirst("A")

    chemin = g.getPath(start,end,prev)

    print("Path from ",start, " to ",end)
    g.printPath(chemin)

    start ="A"
    end = "D"
    print("\nDijkstraa from ",start)
    prev,dist = g.runDijkstra(start)

    chemin = g.getPath(start,end,prev)
    print("Path from ",start, " to ",end)
    g.printPath(chemin)
    print("distance from ",start, " to ",end,dist[end])


if __name__ == '__main__':
    myMainWeightedUndirected()
