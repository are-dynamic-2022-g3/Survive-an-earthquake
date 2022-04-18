import numpy as np
import random
import matplotlib.pyplot as plt


class perso:
    def __init__(self, age, sante, capital, posi):
       #self.sexe = sexe
       self.age = age
       self.sante = sante
       #self.transp = transp
       self.capital = capital
       self.posi = posi

# age entre 0 et 100, sante {0,1} : 0-> handicape ; 1 -> bonne sante, capital {0,1,2,3} : 0 -> pauvre ; 1 -> classe moy ; 2 -> riche ; 3 -> ultra riche.
def append_hab(type_habitation, position, Lhab):
    if type_habitation == 1:
        nb_hab = np.random.randint(2, 20)
        
    if type_habitation == 2:
        nb_hab = np.random.randint(0, 5)
        
    if type_habitation == 3:
        nb_hab = np.random.randint(5, 15)
        
    if type_habitation == 4:
        nb_hab = np.random.randint(10, 20)
        
    if type_habitation == 5:
        nb_hab = np.random.randint(50, 150)
        
    for i in range (nb_hab):
        personne = perso(0,0,0,0)
        
        #Age : hasard entre 10 et 80
        personne.age = np.random.randint(10,80)
        
        # Classe sociale : en fonction du batiment ou on habite
        if type_habitation == 1 or type_habitation == 3:
            r1 = np.random.randint(5)
            if r1<=3:
                personne.capital = 0
            
            else :
                personne.capital = 1
                
        if type_habitation == 2 :
            r2 = np.random.randint(11)
            if r2<=5:
                personne.capital = 1
            
            elif r2<=9:
                personne.capital = 2
            
            else :
                personne.capital = 3
        
        if type_habitation == 4 :
            r3 = np.random.randint(11)
            if r3<=7:
                personne.capital = 1
            
            else:
                personne.capital = 2
        
        if type_habitation == 5 :
            r4 = np.random.randint(51)
            if r4<=40:
                personne.capital = 1
            
            elif r4<=49:
                personne.capital = 2
            
            else :
                personne.capital = 3
        
        # Sante : 1% chance d'etre handicape
        r5 = np.random.randint(101)
        if r5 == 1:
            personne.sante = 0
        
        else : 
            personne.sante = 1
        
        personne.posi = position
        Lhab.append(personne)
            
#Aurelien
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
        """plt.imshow(rgrid)
        plt.show()"""
    return rgrid

def densite1(M,dm,dp):
    n=len(M)
    m = n//2
    for i in range(m+1):
        for j in range(m+1):
            if(M[i][j]>0):
                L=[M[i][j]]*(M[i][j]*dm)+[0]*dp
                M[i][j]=random.choice(L)
                M[n-i-1][n-j-1]=M[i][j]
                M[n-i-1][j]=M[i][j]
                M[i][n-j-1]=M[i][j]
    """plt.imshow(M)
    plt.show()"""

def densite2(M,dm,dp):
    #plus lent
    n=len(M)
    m = n//2
    for i in range(m+1):
        for j in range(m+1):
            if(M[i][j]>0):
                L=[M[i][j]]*(M[i][j]*dm)+[0]*dp
                M[i][j]=random.choice(L)
                M[n-i-1][n-j-1]=random.choice(L)
                M[n-i-1][j]=random.choice(L)
                M[i][n-j-1]=random.choice(L)
    """plt.imshow(M)
    plt.show()"""
    
def cityRoad1(city,e, graph=False):
    n=len(city)
    x = np.zeros((n,1), dtype=int) 
    M = n//2
    j = 1
    A = 1
    while(A<M):
        x[M+A] = -1
        x[M-A] = -1
        A += j
        j += e
    #changer aussi les valeurs de city en même temps
    road, roadT = np.meshgrid(x, x)
    road = road+roadT
    if graph:
        print(road)
        """plt.imshow(road)
        plt.show()"""
    return road

def cityRoad2(city,e, graph=False):
    n=len(city)
    x = np.zeros((n,1), dtype=int) 
    M = n//2
    A = 1
    while(A<M):
        x[M+A] = -1
        x[M-A] = -1
        A += e
    #changer aussi les valeurs de city en même temps
    road, roadT = np.meshgrid(x, x)
    road = road+roadT
    if graph:
        """plt.imshow(road)
        plt.show()"""
    return road

def matrice_up(M1,M2):
    #lent
    """plt.imshow(M2)
    plt.show()"""
    for i in range(len(M1)):
        for j in range(len(M1)):
            if(M1[i][j])!=0:
                M2[i][j]=M1[i][j]
    """plt.imshow(M2)
    plt.show()"""

def matrice_up2(M1,M2):
    #plus rapide mais symmétrique
    """plt.imshow(M2)
    plt.show()"""

    for i in range(len(M1)):
        if(M1[0, i])!=0:
                M2[:, i]=M1[: ,i]
                M2[i, :]=M1[i, :]
    """plt.imshow(M2)
    plt.show()"""

            
def build1(M):
    #version symmétrique
    n=len(M)
    m = n//2
    for i in range(m+1):
        for j in range(m+1):
            if((M[i][j]>0) and (M[i][j]!=5)):
                M[i][j]=random.choice([M[i][j],random.randint(M[i][j]-1,M[i][j]+1)])
                M[n-i-1][n-j-1]=M[i][j]
                M[n-i-1][j]=M[i][j]
                M[i][n-j-1]=M[i][j]
    """plt.imshow(M)
    plt.show()"""

def build2(M):
    #version lente
    n=len(M)
    m = n//2
    for i in range(m+1):
        for j in range(m+1):
            if((M[i][j]>0) and (M[i][j]!=5)):
                M[i][j]=random.choice([M[i][j],random.randint(M[i][j]-1,M[i][j]+1)]) 
                M[n-i-1][n-j-1]=random.choice([M[n-i-1][n-j-1],random.randint(M[n-i-1][n-j-1]-1,M[n-i-1][n-j-1]+1)])
                M[n-i-1][j]=random.choice([M[n-i-1][j],random.randint(M[n-i-1][j]-1,M[n-i-1][j]+1)])
                M[i][n-j-1]=random.choice([M[i][n-j-1],random.randint(M[i][n-j-1]-1,M[i][n-j-1]+1)])
            if(M[i][j]>=5):
                M[i][j]=random.choice([M[i][j],random.randint(M[i][j]-1,M[i][j])]) 
                M[n-i-1][n-j-1]=random.choice([M[n-i-1][n-j-1],random.randint(M[n-i-1][n-j-1]-1,M[n-i-1][n-j-1])])
                M[n-i-1][j]=random.choice([M[n-i-1][j],random.randint(M[n-i-1][j]-1,M[n-i-1][j])])
                M[i][n-j-1]=random.choice([M[i][n-j-1],random.randint(M[i][n-j-1]-1,M[i][n-j-1])])
    """plt.imshow(M)
    plt.show()"""
 
def HAP(M):
    Mhauteur = np.zeros((len(M),len(M)), dtype=int) 
    Mage = np.zeros((len(M),len(M)), dtype=int) 
    Mres = np.zeros((len(M),len(M)), dtype=int)
    Lhab = []
    n = len(M)
    m = n//2
    d = { 1:(6,12), 2:(7,12), 3:(8,16), 4:(12,20), 5:(30,120)}
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]>5:
                M[i][j]=5
            if M[i][j] > 0:
                #print(M[i][j])
                Min = d[M[i][j]][0]
                Max = d[M[i][j]][1]
                Mhauteur[i][j] = random.randint(Min,Max)
                Mage[i][j] = random.randint(30,70)
                Mres[i][j] = random.randint(1,10)//M[i][j]
                
                #caracs habitant
                append_hab(M[i][j],(i,j),Lhab)
                
                
    Hc = [[random.randint(m-n//6,m+n//6+1),random.randint(m-n//6,m+n//6+1)] for i in range(n//30)]
    #print(Hc)
    for c in Hc:
        for x in range(c[0]-(n//30+1),c[0]+(n//30+1)):
            for y in range(c[1]-(n//30+1),c[1]+(n//30+1)):
                if (M[x][y] > 0) and (M[x][y]!=5):
                    Mage[x][y] = random.randint(70,130)
    #print(Mhauteur)
    """plt.imshow(Mhauteur)
    plt.show()
    plt.imshow(Mage)
    plt.show()"""
    return Mage,Mhauteur,Mres,Lhab

def cityground(n,m,d):
    matrice = np.zeros((n,n), dtype=int) 
    grid = matrice
    rgrid = matrice
    x = random.randint(-d,len(matrice)-1+d)
    y = random.randint(-d,len(matrice)-1+d)
    M = [x,y]
    circles = {}
    for i in range(1,round((len(matrice))*m*2)):
        circles[i] = [[M[0],M[1]],i]
    
    xx = np.arange(grid.shape[0])
    yy = np.arange(grid.shape[1])
    for val in circles.values():
        radius = val[1]
        inside = (xx[:, None] - val[0][0])**2 + (yy - val[0][1])**2 <= radius**2
        grid = grid | inside
        rgrid += grid
    """plt.imshow(rgrid)
    plt.show()"""
    for i in range(len(rgrid)*(len(rgrid)//2)):
        x = random.randint(0,len(rgrid)-1)
        y = random.randint(0,len(rgrid)-1)
        cgt = random.randint(-1,1)
        if rgrid[x][y]!=0:
            rgrid[x][y] += cgt
        else:
            rgrid[x][y] += abs(cgt)
    #print(rgrid)
    """plt.imshow(rgrid)
    plt.show()"""
    return rgrid

def Earthquake(M, MAge, MHeight, MRes, m):   #matrice ville, magnitude 
    n=len(M)
    MGround = cityground(len(M),m, n*10)
    M = ((m//6)*MGround)+(MAge//8)+(MHeight//6)+MRes*4
    M = (M/40).round(decimals=1)
    M = M-np.min(M)
    #print(M, "\nmax:", round(np.max(M),2) , " mean:", round(np.mean(M),2))
    """ plt.imshow(M)
    plt.show()
    plt.imshow(M.round(decimals=0))
    plt.show()"""
    
    
    """for i in range(len(M)):
        for j in range(len(M)):
            
            #détruire en fct de age et taille 
            print("n")"""
    return M

def equation(perso, mat_magnitude, chance_mort_init):
    x, y = perso.posi
    ratio_magnitude = mat_magnitude[x][y]
    if perso.sante == 0:
        ratio_handicap = 2
    else:
        ratio_handicap = 1
    if perso.age >= 75:
        ratio_age = 2.3
    elif perso.age >= 40:
        ratio_age = 1.5
    elif perso.age <= 15:
        ratio_age = 1.2
    else:
        ratio_age = 1
    if perso.capital == 3:
        ratio_capital = 0.5
    else:
        ratio_capital = 1.1
    chance_m = ((chance_mort_init*ratio_capital*ratio_age* ratio_handicap*ratio_magnitude)/np.max(mat_magnitude)*2.5)/2
    return chance_m


def simulation_richesse(taille_v,chance_mort_init):
    g = cityConcentric(taille_v,taille_v)
    
    build2(g)

    densite2(g,3,4)

    r = cityRoad2(g,5,False)  
    matrice_up2(r,g)
 
    MAge, MHauteur, MRes, Lhab = HAP(g)

    M = Earthquake(g,MAge, MHauteur, MRes, 8)
    
    liste_chances = [[],[],[],[]]
    for i in Lhab:
        if i.capital == 0:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[0].append(1)
            else:
                liste_chances[0].append(equation(i, M, chance_mort_init))
        if i.capital == 1:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[1].append(1)
            else:
                liste_chances[1].append(equation(i, M, chance_mort_init))
        if i.capital == 2:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[2].append(1)
            else:
                liste_chances[2].append(equation(i, M, chance_mort_init))
        if i.capital == 3:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[3].append(1)
            else:
                liste_chances[3].append(equation(i, M, chance_mort_init))
    """for j in range(4):
        plt.plot(liste_chances[j])
    plt.show()"""
    return liste_chances


def simulation_mult_rich(taille_v,chance_mort_init,iterations):
    Lmoy = [[],[],[],[]]
    for i in range(iterations):
        M = simulation_richesse(taille_v, chance_mort_init)
        Lmoy[0].append(np.mean(M[0]))
        Lmoy[3].append(np.mean(M[3]))
        Lmoy[2].append(np.mean(M[2]))
        Lmoy[1].append(np.mean(M[1]))
    plt.subplot(1, 2, 1)
    plt.plot(Lmoy[0], 'r', label = "pauvres")
    plt.plot(Lmoy[1], 'm', label = "classe moyenne")
    plt.plot(Lmoy[2], 'y', label = "riches")
    plt.plot(Lmoy[3], 'c', label = "ultra-riches")
    plt.ylim(0,1)
    plt.subplot(1, 2, 2)
    plt.plot([0,iterations], [np.mean(Lmoy[0]),np.mean(Lmoy[0])], 'r--', label = "pauvres")
    plt.plot([0,iterations], [np.mean(Lmoy[1]),np.mean(Lmoy[1])], 'm--', label = "classe moyenne")
    plt.plot([0,iterations], [np.mean(Lmoy[2]),np.mean(Lmoy[2])], 'y--', label = "riches")
    plt.plot([0,iterations], [np.mean(Lmoy[3]),np.mean(Lmoy[3])], 'c--', label = "ultra-riches")
    plt.ylim(0,1)
    plt.legend()
    plt.show()
    return Lmoy




def simulation_age(taille_v,chance_mort_init):
    #simulation simple en fonction de l'age
    g = cityConcentric(taille_v,taille_v)
    
    build2(g)

    densite2(g,3,4)

    r = cityRoad2(g,5,False)  
    matrice_up2(r,g)
 
    MAge, MHauteur, MRes, Lhab = HAP(g)

    M = Earthquake(g,MAge, MHauteur, MRes, 8)
    
    liste_chances = [[],[],[],[]]
    for i in Lhab:
        if 0 < i.age <= 15:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[0].append(1)
            else:
                liste_chances[0].append(equation(i, M, chance_mort_init))
        if 15 < i.age <= 40:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[1].append(1)
            else:
                liste_chances[1].append(equation(i, M, chance_mort_init))
        if 60 < i.age <= 75:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[2].append(1)
            else:
                liste_chances[2].append(equation(i, M, chance_mort_init))
        if 75 < i.age:
            if equation(i, M, chance_mort_init) >= 1:
                liste_chances[3].append(1)
            else:
                liste_chances[3].append(equation(i, M, chance_mort_init))
            
    """for j in range(4):
        plt.plot(liste_chances[j])
    plt.show()"""
    return liste_chances


def simulation_mult_age(taille_v,chance_mort_init,iterations):
    #simuation multiple en fonction de l'age et affiche les graphes
    Lmoy = [[],[],[],[]]
    for i in range(iterations):
        M = simulation_age(taille_v, chance_mort_init)
        Lmoy[0].append(np.mean(M[0]))
        Lmoy[1].append(np.mean(M[1]))
        Lmoy[2].append(np.mean(M[2]))
        Lmoy[3].append(np.mean(M[3]))
    plt.subplot(1, 2, 1)
    plt.plot(Lmoy[0], 'r', label = "jeunes")
    plt.plot(Lmoy[1], 'm', label = "adultes")
    plt.plot(Lmoy[2], 'y', label = "personnes agées")
    plt.plot(Lmoy[3], 'c', label = "personnes très agées")
    plt.ylim(0,1)
    plt.subplot(1, 2, 2)
    plt.plot([0,iterations], [np.mean(Lmoy[0]),np.mean(Lmoy[0])], 'r--', label = "jeunes")
    plt.plot([0,iterations], [np.mean(Lmoy[1]),np.mean(Lmoy[1])], 'm--', label = "adultes")
    plt.plot([0,iterations], [np.mean(Lmoy[2]),np.mean(Lmoy[2])], 'y--', label = "personnes agées")
    plt.plot([0,iterations], [np.mean(Lmoy[3]),np.mean(Lmoy[3])], 'c--', label = "personnes très agées")
    plt.ylim(0,1)
    plt.legend()
    plt.show()
    return Lmoy

"""g = cityConcentric(100,100)
plt.imshow(g)
plt.show()
print("buildings")
#build1(g)
build2(g)
print("densité")
densite2(g,3,4)
print("road")
r = cityRoad2(g,5,False)  
matrice_up2(r,g)
n=len(g)
m = n//2
print(g[m-5:m+6,m-5:m+6])
print("hauteur et age")
MAge, MHauteur, MRes, Lhab = HAP(g)
M = Earthquake(g,MAge, MHauteur, MRes, 8)"""

#simulation1(25, 0.3)
print("Magnitude 3 et 8 en fonction de la richesse")
simulation_mult_rich(50, 0.3, 50)
simulation_mult_rich(50, 0.8, 50)
print("Magnitude 3 et 8 en fonction de l'age")
simulation_mult_age(50, 0.3, 50)
simulation_mult_age(50, 0.8, 50)


"""
import matplotlib.pyplot as plt
n=100
m=100
grid = np.zeros((n,m), dtype=np.bool)
square_length = 0.5
M = (n//2,m//2)
print(M)
circles = {'c1':[[M[0],M[1]],1.5]}
# Generate arrays of indices/coordiates so we can do the
# calculations the Numpy way, without resorting to loops
# I always get the index order wrong so double check...
xx = np.arange(grid.shape[0])
yy = np.arange(grid.shape[1])
for val in circles.values():
radius = val[1]
# same index caveat here
# Calling Mr Pythagoras: Find the pixels that lie inside this circle
inside = (xx[:, None] - val[0][0])**2 + (yy - val[0][1])**2 <= radius**2
# do grid & inside and initialize grid with ones for intersection instead of union
grid = grid | inside
plt.imshow(grid)
plt.show()"""
