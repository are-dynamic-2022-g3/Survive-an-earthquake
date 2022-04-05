#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:04:04 2022

@author: 21100696
"""

#0 : route
#1 : maison 6-12
#2 : residence 7-12
#3 : usine 8-16
#4 : immeuble 12-20
#5 : gratte ciel 30-120

import numpy as np
import random
import matplotlib.pyplot as plt

def cityConcentric(n,m, graph=False):
    #len(matrice) >= 10
    """Creer une ville sur un modele concentrique de taille n*m"""
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
    """Supprime aleatoirement certains batiments, pour avoir un modele se rapprochant de la realite, densite moins => plus de batiment 5, densite plus"""
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
    """Creer une matrice pour les routes"""
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
    """Applique la matrice des routes sur la matrice de la ville"""
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
    """Fragmente legerement le centre ville"""
    #version symmétrique
    n=len(M)
    m = n//2
    for i in range(m+1):
        for j in range(m+1):
            if(M[i][j]>0):
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
            if(M[i][j]>0 & M[i][j]!=5):
                M[i][j]=random.choice([M[i][j],random.randint(M[i][j]-1,M[i][j]+1)])
                M[n-i-1][n-j-1]=random.choice([M[n-i-1][n-j-1],random.randint(M[n-i-1][n-j-1]-1,M[n-i-1][n-j-1]+1)])
                M[n-i-1][j]=random.choice([M[n-i-1][j],random.randint(M[n-i-1][j]-1,M[n-i-1][j]+1)])
                M[i][n-j-1]=random.choice([M[i][n-j-1],random.randint(M[i][n-j-1]-1,M[i][n-j-1]+1)])
            if(M[i][j]==5):
                M[i][j]=random.choice([M[i][j],random.randint(M[i][j]-1,M[i][j])])
                M[n-i-1][n-j-1]=random.choice([M[n-i-1][n-j-1],random.randint(M[n-i-1][n-j-1]-1,M[n-i-1][n-j-1])])
                M[n-i-1][j]=random.choice([M[n-i-1][j],random.randint(M[n-i-1][j]-1,M[n-i-1][j])])
                M[i][n-j-1]=random.choice([M[i][n-j-1],random.randint(M[i][n-j-1]-1,M[i][n-j-1])])
    plt.imshow(M)
    plt.show()
    
def hauteur(M):
    Mhauteur = np.zeros((len(M),len(M)), dtype=int) 
    d = { 1:(6,12), 2:(7,12), 3:(8,16), 4:(12,20), 5:(30,120)}
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > 0:
                #print(M[i][j])
                Min = d[M[i][j]][0]
                Max = d[M[i][j]][1]
                Mhauteur[i][j] = random.randint(Min,Max)
    print(Mhauteur)
    plt.imshow(Mhauteur)
    plt.show()
            
g = cityConcentric(10,10)
plt.imshow(g)
plt.show()

print("buildings")
#build1(g)
build2(g)

print("densité")
densite2(g,1,2)

print("road")
r = cityRoad2(g,5,False)  
matrice_up2(r,g)
 
print("hauteur")
hauteur(g)



n=len(g)
m = n//2
print(g[m-4:m+5,m-4:m+5])
#matrice_up(r,g) 
