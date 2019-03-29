## Cours 2 : Philo et Dijkstraa

### Philo :
Que met on dans les graphes ?

Le plus souvent les sommets sont :
- des objets du "monde réel" (des villes pour de la recherche de chemin ou des
personnes pour de la recherche généalogique)
- des configurations.

Quand vous aurez un problème à résoudre, et que vous soupçonnez que des graphes
puissent vous fournir  

### Dijkstraa


Le principe, je vous l'ai expliqué en cours.

le code :
```python
toDo = [start]
alreadyDone = []
previous ={}
distances = {start : 0.0}

while toDo :
    current=g._getMinDistance(toDo, distances)
    #print ("processing", str(current))

    for s in g.getNeighbors(current) :
        #print (s)
        if (not s in alreadyDone):
            # compute the distance of the new path
            newDist = distances[current]+g.getArcWeight(current,s)
            ## did we see it before ?
            if not s in distances.keys():
                previous[s]=current
                distances[s]= newDist
                toDo.append(s)
            else :
                oldDist = distances[s]
                if newDist < oldDist :
                    previous[s]=current
                    distances[s]= newDist

    toDo.remove(current)
    alreadyDone.append(current)

```
