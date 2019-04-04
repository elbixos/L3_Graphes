
import GraphLib.WeightedUndirectedGraph

def myMainWeightedUndirected():
    g = GraphLib.WeightedUndirectedGraph.WeightedUndirectedGraph(name="GwadaRoads")

    g.addArc("Moule", "St Francois", 27)
    g.addArc("St Francois", "St Anne",21)
    g.addArc("St Anne","Gosier",11)
    g.addArc("Gosier", "La Pwent",10)
    g.addArc("Morne a l eau", "Moule",13)
    g.addArc("Morne a l eau", "Abymes",22)
    g.addArc("La Pwent", "Abymes",25)

    g.addArc("La Pwent", "Jarry",13)
    g.addArc("Abymes", "Jarry",14)

    g.addArc("Jarry","Baie Mahaut",9)
    g.addArc("Baie Mahaut", "Petit Bourg",9)
    g.addArc("Petit Bourg","Capesterre",19)
    g.addArc("Capesterre","Trois Rivieres",18)
    g.addArc("Trois Rivieres","Basse Terre",20)
    g.addArc("Basse Terre","Bouillante",25)
    g.addArc("Bouillante","Pointe Noire",4)
    g.addArc("Pointe Noire","Deshaies",20)
    g.addArc("Deshaies","Ste Rose",17)
    g.addArc("Ste Rose","Baie Mahaut",27)

    g.addArc("Jarry","Pointe Noire",32)



    g.addArc("Capesterre de MG","Grand Bourg", 15)
    g.addArc("Grand Bourg", "St Louis",15)
    g.addArc("Capesterre de MG","St Louis", 20)

    g.toDot()


    g.toDot("gwadaRoads.dot")

    # start ="Le Moule"
    # end = "Basse Terre"
    # print("\nBreadthFirstSearch from ",start)
    # prev = g.runBreadthFirst(start)
    #
    # chemin = g.getPath(start,end,prev)
    #
    # print("Path from ",start, " to ",end)
    # g.printPath(chemin)
    #
    # print("\nDijkstraa from ",start)
    # prev,dist = g.runDijkstra(start)
    #
    # chemin = g.getPath(start,end,prev)
    # print("Path from ",start, " to ",end)
    # g.printPath(chemin)
    # print("distance from ",start, " to ",end,dist[end])


if __name__ == '__main__':
    myMainWeightedUndirected()
