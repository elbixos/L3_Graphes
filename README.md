# L3_Graphes
Cours de Graphes et Applications, université des Antilles


## Visualisation des graphes.
Vous verrez que créer des petits graphes sera relativement facile avec notre
librairie. Mais il nous faudra surtout visualiser ces graphes pour voir si nous avons
bien crée le graphe que nous voulions.

Faire une librairie de visualisation de graphes efficace est très difficile
(C'est un domaine de recherche en informatique). Nous allons donc utiliser une
librairie existante, parmi les plus utilisées au monde : **graphviz**

Pour la visualisation des graphes, chacun de nos graphes devra pouvoir être sauvegardé
dans un fichier texte (format **.dot**) qui sera utilisé par la librairie
**graphviz** pour la visualisation.
Tout les fichiers d'exemples génère un fichier **.dot** que vous pourrez tester.

La librairie s'installe facilement sur les machines linux.
- Si c'est votre cas, vous pourrez utiliser le script **lancerGraphviz.sh** qui
transforme chaque fichier **.dot** en fichier png.
- Si vous ne pouvez pas installer **graphviz**, vous utiliserez une version
online de graphviz. Il en existe beaucoup.
[http://www.webgraphviz.com/](http://www.webgraphviz.com/) en est un bon exemple.
Dans ce cas : ouvrez un fichier **.dot**, copiez son contenu et collez le dans
le formulaire de la page dont je viens de vous fournir l'adresse.
Appuyez sur "Generate Graph" et observez votre graphe...



## La nouvelle librairie de graphes (en Python)

Pour le moment sont implémentés :

- les graphes orientés
- les graphes non orientés
- les graphes orientés valués
- les graphes non orientés valués

La librairie est dans [Sources/GraphLib/](Sources/GraphLib)
Chaque type de graphe à son fichier.
Par exemple le graphe orienté est codé dans
[Sources/GraphLib/DirectedGraph.py](Sources/GraphLib/DirectedGraph.py).

Cette classe est exploitée par un main dans [Sources/GraphLib/](Sources/GraphLib).

On pourra donc tester les graphes orientés avec le main contenu dans
[Sources/testDirectedGraph.py](Sources/testDirectedGraph.py)
Vous pouvez lancer ce fichier qui vous générera un fichier **.dot** fonctionnel.
Je vous invite à regarder le contenu d'un fichier de type **.dot**...

## documentation de la librairie :

La librairie est autodocumentée. Le code contient des commentaires de type **docstring** que j'espere relativement clairs.

Mais ce type de documentation permet aussi de générer une documentation qui permet de se servir des classes sans meme regarder le code.

Cette documentation est visible depuis le fichier [Sources/docs/_build/html/index.html](Sources/docs/_build/html/index.html)

## Illustration du parcours en largeur :
Au delà des parcours de Graphes dans des vrais graphes,
il arrive que l'on utilise ces algorithmes sans même disposer d'une structure
de graphes. C'est souvent le cas en Path Finding : la recherche d'un chemin dans un
labyrinthe, que l'on retrouve souvent dans des jeux.

Lancez le programme dont le code est dans [Sources/mainLabSimple.py](Sources/mainLabSimple.py).
vous comprendrez mieux ensuite.

L'interface est minimaliste :

- cliquez sur une case pour creer un mur ou en supprimer un.
- appuyez sur "s" (start) puis cliquez sur une case pour définir le point de départ
- appuyez sur "e" (end) puis cliquez sur une case pour définir l'arrivée
- appuyez sur "r" (run) pour lancer la recherche de chemin
- appuyez sur "n" (next) pour lancer la recherche de chemin step by step

pour voir la table des predecesseurs en construction,
lancer la recherche en step by step.


Quel est le graphe qui est caché la dessous ?
