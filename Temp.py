import numpy as np
import random
import matplotlib.pyplot as plt

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
        plt.imshow(rgrid)
        plt.show()
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
    plt.imshow(M)
    plt.show()

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
    plt.imshow(M)
    plt.show()
    
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
        plt.imshow(road)
        plt.show()
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
        plt.imshow(road)
        plt.show()
    return road

def matrice_up(M1,M2):
    #lent
    plt.imshow(M2)
    plt.show()
    for i in range(len(M1)):
        for j in range(len(M1)):
            if(M1[i][j])!=0:
                M2[i][j]=M1[i][j]
    plt.imshow(M2)
    plt.show()

def matrice_up2(M1,M2):
    #plus rapide mais symmétrique
    plt.imshow(M2)
    plt.show()

    for i in range(len(M1)):
        if(M1[0, i])!=0:
                M2[:, i]=M1[: ,i]
                M2[i, :]=M1[i, :]
    plt.imshow(M2)
    plt.show()

            
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
    plt.imshow(M)
    plt.show()

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
    plt.imshow(M)
    plt.show()
 
def HA(M):
    Mhauteur = np.zeros((len(M),len(M)), dtype=int) 
    Mage = np.zeros((len(M),len(M)), dtype=int) 
    Mres = np.zeros((len(M),len(M)), dtype=int) 
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
    Hc = [[random.randint(m-n//6,m+n//6+1),random.randint(m-n//6,m+n//6+1)] for i in range(n//30)]
    print(Hc)
    for c in Hc:
        for x in range(c[0]-(n//30+1),c[0]+(n//30+1)):
            for y in range(c[1]-(n//30+1),c[1]+(n//30+1)):
                if (M[x][y] > 0) and (M[x][y]!=5):
                    Mage[x][y] = random.randint(70,130)
    print(Mhauteur)
    plt.imshow(Mhauteur)
    plt.show()
    plt.imshow(Mage)
    plt.show()
    return Mage,Mhauteur,Mres

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
    plt.imshow(rgrid)
    plt.show()
    for i in range(len(rgrid)*(len(rgrid)//2)):
        x = random.randint(0,len(rgrid)-1)
        y = random.randint(0,len(rgrid)-1)
        cgt = random.randint(-1,1)
        if rgrid[x][y]!=0:
            rgrid[x][y] += cgt
        else:
            rgrid[x][y] += abs(cgt)
    print(rgrid)
    plt.imshow(rgrid)
    plt.show()
    return rgrid

def Earthquake(M, MAge, MHeight, MRes, m):   #matrice ville, magnitude 
    n=len(M)
    MGround = cityground(len(M),m, n*10)
    M = ((m//6)*MGround)+(MAge//8)+(MHeight//6)+MRes*4
    M = (M/40).round(decimals=1)
    M = M-np.min(M)
    print(M, "\nmax:", round(np.max(M),2) , " mean:", round(np.mean(M),2))
    plt.imshow(M)
    plt.show()
    plt.imshow(M.round(decimals=0))
    plt.show()
    """for i in range(len(M)):
        for j in range(len(M)):
            
            #détruire en fct de age et taille 
            print("n")"""
 
g = cityConcentric(100,100)
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
MAge, MHauteur, MRes = HA(g)

Earthquake(g,MAge, MHauteur, MRes, 8)
#matrice_up(r,g) 
#aurelien
