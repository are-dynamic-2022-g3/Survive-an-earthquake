## Projet ARE 2022: Survive An Earthquake

  Un séisme dure en moyenne une minute, c’est plus que le temps qu’il vous faudra pour lire cette introduction. Notre projet d’ARE consiste à modéliser ainsi qu’analyser l’évolution d’une population lambda durant l’occurrence d’un tremblement de terre en ville. L’objectif de ce projet est d’identifier les différents facteurs qui ont un impact sur les chances de survie durant un séisme. On regardera seulement les effets primaires (sur un court lapse de temps). Les enjeux de notre modèle sont de comprendre comment vivre dans un quartier plus développé peut limiter le nombres de victimes. Nous nous intéresserons aussi à des facteurs corrélés tel que la densité de la population étudié, l’age moyen, la hauteur d’habitation moyenne… Cette étude nous permettra de construire un modèle assez réaliste avec lequel il nous sera facile d’isoler des facteurs pour être sûr de prouver notre hypothèse.

### Blog

Voici le travail que nous avons fais chaque semaine

### Description du projet

Nous avons choisi de travailler sur des Matrices et d'utiliser le modèle de Burgess, la fonction city concentric nous permet de diviser notre matrice en plusieur cercles.
```py
def cityConcentric(n,m, graph=False):
    #len(matrice) >= 10
    if n%2 == 0:
        n=n+1
        m=m+1
    grid = np.zeros((n,m), dtype=int) 
    rgrid = np.zeros((n,m), dtype=int) 
    M = [n//2,n//2]
        
    circles = {}
    for i in range(n//12,n//2,n//10):
        circles[i] = [[M[0],M[1]],i]
    
    xx = np.arange(grid.shape[0])
    yy = np.arange(grid.shape[1])
    for val in circles.values():
        radius = val[1]
        inside = (xx[:, None] - val[0][0])**2 + (yy - val[0][1])**2 <= radius**2
        grid = grid | inside
        rgrid += grid
    if graph:
        plt.imshow(rgrid)
        plt.show()
    return rgrid
```

voici le résultat de l'appel `cityConcentric(100,100, True)`: ![image](https://user-images.githubusercontent.com/99738357/163983314-b5af5387-a496-4715-94f9-5afcf9927ca8.png)

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/are-dynamic-2022-g3/Survive-an-earthquake/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
