
## Les Graphes : a quoi ça sert ?

Je n'ai pas encore eu le temps de rédiger complètement ce cours, voici donc les
grandes lignes de ce que nous avons vu en cours.

Graphes, a quoi ca sert ?

des algos de parcours : quel objectif ?
relation locale -> relation globale

### Fonctionnement général des parcours

Imaginons un graphe *g*, dans lequel je veuille faire un parcours avec un départ
depuis le sommet *start*

Nous avons vu quel était l'algorithme général des parcours :
il nous faut 2 ensembles :
- **toDo** : les sommets dont qu'on a croisé, mais pas traité
- **alreadyDone** : les sommets qu'on a traité.

A la fin de l'execution, **alreadyDone** contiendra l'ensemble des sommets
visités pendant le parcours.

J'ai, dans le code suivant inventé les méthodes
- *getCurrent*
- *addWhereNeeded*
qui vont varier d'un parcours à l'autre.

```python
toDo = [start]

alreadyDone = set() # a HashSet...

while toDo :
    current=toDo.getCurrent(toDo)

    for s in g.getNeighbors(current) :
        if (not s in toDo) and (not s in alreadyDone):
            toDo.addWhereNeeded(s)

    toDo.remove(current)
    alreadyDone.add(current)

```

### Retenir les chemins : La table de prédécesseurs.
Savoir quels sommets peuvent être atteints est important, mais connaitre un
chemin pour les atteindre, c'est mieux !

Or un parcours nous indique, pour chaque sommet, comment l'atteindre (la
première fois qu'on le voit), depuis le sommet **current**.
C'est cette information que l'on va retenir dans une **table de prédécesseurs**.

AJOUTER Illustration et fonctionnement de cette table, vue en cours.




A la fin de l'execution, **alreadyDone** aura comme clefs l'ensemble des sommets
visités pendant le parcours et la valeur associée à un sommet *k* sera le sommet
par lequel on accède à *k* lors du chemin de *start* à *k*.

Le code serait alors le suivant :
```python
toDo = [start]

alreadyDone = set() # a HashSet...
previous ={}

while toDo :
    current=toDo.getCurrent(toDo)

    for s in g.getNeighbors(current) :
        if (not s in toDo) and (not s in alreadyDone):
            toDo.addWhereNeeded(s)
            previous[s]=current

    toDo.remove(current)
    alreadyDone.add(current)

```

### Parcours en largeur
J'ai détaillé son fonctionnement en cours,
je résumerais en disant que :
- toDo est une File
- le parcours en largeur fournit le plus cours chemin en termes de nombres d'arêtes.

Pour implémenter une File avec des tableaux, on peut par exemple :
- retirer des elements en tête de tableau (le prochain élément à traiter)
- ajouter des élements en fin de tableau (le nouvel élément arrivant dans la file)

```python
toDo = [start]
# in BreadthFirstSearch algorithm, toDo is a FIFO.
# beginning of the queue is at index 0 of the list.
# new elements are put at the end of the list

alreadyDone = set() # a HashSet...
previous ={}

while toDo :
    current=toDo[0]
    #print ("processing", str(current))

    for s in g.getNeighbors(current) :
        #print (s)
        if (not s in toDo) and (not s in alreadyDone):
            previous[s]=current
            toDo.append(s)

    toDo.remove(current)
    alreadyDone.add(current)

```

### Parcours en profondeur
J'ai détaillé son fonctionnement en cours,
je résumerais en disant que :
- toDo est une Pile

Pour implémenter une File avec des tableaux, on peut par exemple :
- retirer des elements en tête de tableau (le prochain élément à traiter)
- ajouter des élements en tête de tableau (le nouvel élément arrivant dans la file)
