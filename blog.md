## Travail effectué 

### Semaine 1
Semaine brainstorming !
Cette semaine nous avons finalisé nos réflexions sur notre projet, décidé d'une problématique et d'une approche du thème plutôt originale :
la plupart des travaux que nous avons pu trouver traitaient des réactions des populations et de leurs déplacements dans et en dehors d'une ville après un tremblement de terre. Mais les articles qui traitaient du laps de temps cours durant le séisme n'incluent généralement pas tous les paramètres que nous voulons inclure dans nos modèles.
Ainsi un travail approfondi sur nos sources est nécessaire lors de la deuxième semaine du projet.
### Semaine 2
Cette semaine nous avons fait la bibliographie de notre projet. Après avoir trouver un article à l'aide de mots clés, nous nous mettons d'accord sur le fait d'intégrer cette source à notre bibliographie ou non. C'est un processus de sélection au sein du groupe et d'analyse des sources afin qu'elles soient en accord à notre plan. De plus, nous avons aussi alimenter/mis à jour les pages du Github nécessaires au développement du projet.
### Semaine 3
Cette semaine, nous avons débattu de notre modèle et de la meilleure façon de l'implémenter. Nous avons choisi de commencer par le modéle le plus simple, modéle concentrique. Nous avons représenté notre ville par une multitude de matrices carré qui correspondent à la propagation des ondes, les différents batiments, la hauteur et l'age de ces structures. 

Voici notre modèle de ville basé sur le modèle de Burgess:

![image](https://user-images.githubusercontent.com/99736848/163983372-75105150-d76c-4f73-895b-5c11f4fe63da.png)


Voici ci dessous notre matrice de propagation des ondes:

![image](https://user-images.githubusercontent.com/99737904/159502319-f2776ada-3f9d-4fe0-b899-7c6b866b3708.png)

### Semaine 4
Cette semaine, nous avons continué de travailler sur notre modèle, en particulier la création des routes et des habitants de la ville, en leur affectant des données qui impacteront leur chances de survie potentielle, telles qu'un âge, un sexe mais également leur localisation et autres. 

Voici ci dessous notre matrice de ville (1000\*1000) selon le modèle de Burgess (que nous avons modifier pour qu'il soit plus réaliste inversion des zones industrielles et zones de logements/immeubles):

![image](https://user-images.githubusercontent.com/99738357/160619688-8f34f8a0-55be-4c67-93f2-d22166d5a8a9.png)

Voici ci dessous notre matrice de hauteur des batiments de la ville (1000\*1000):

![image](https://user-images.githubusercontent.com/99738357/160619650-5b06cc97-0826-4af8-aef6-c7b75cf7f734.png)

10000\*10000 (rien à ajouter)

![image](https://user-images.githubusercontent.com/99738357/160628971-b6ba71a8-9550-4655-bb51-0a27d09d4d9d.png)


[Retour à la page principale](https://github.com/are-dynamic-2022-g3/Survive-an-earthquake)


### Semaine 5
Cette semaine, nous avons modifié quelques parties de notre code, notamment les caractéristiques des habitants de la ville car nous avons trouvé de nouvelles informations pertinentes qui vont nous permettre de mieux faire fonctionner notre projet. Ainsi, nous avons surtout améliorer les parties du code que nous avions déjà pour s'assurer que tout fonctionne bien.

### Semaine 6
Cette semaine nous avons terminé notre code et nous avons effectué des tests et des simulations à partir de celui-ci afin de vérifier si notre hypothèse principale était vérifiée. Ainsi on obtient des graphiques du type : 

Ici sur 50 simulations, on a : 


Graphique du taux de survie non-moyenné et moyenné des victimes en fonction de la richesse des individus et l'âge des individus.

![image](https://user-images.githubusercontent.com/99736848/163979551-df554a24-b209-4bba-b0d7-11f47129e597.png) magnitude 3 en fonction de la richesse

![image](https://user-images.githubusercontent.com/99736848/163979690-e3a8bfe3-599a-48ff-89a6-59eb897b8c73.png) magnitude 8 en fonction de la richesse

![image](https://user-images.githubusercontent.com/99736848/163979765-2cfd1afd-b882-497f-8bea-4655c79d3442.png) magnitude 3 en fonction de l'âge

![image](https://user-images.githubusercontent.com/99736848/163979891-24ccab9f-e21f-4de5-b7b2-1d4c956ab297.png) magnitude 8 en fonction de l'âge




