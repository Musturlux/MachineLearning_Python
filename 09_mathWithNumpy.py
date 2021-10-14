import numpy as np

A = np.random.randint(0, 10, [4,5])

print(A.sum(axis=0))
print(A.sum(axis=1))
print(A.min())
print(A.min(axis=0))
print(A.argmin())
print(A.argmin(axis=1))
print(A.argsort()) #donne l'index pour triee
print(np.cos(A)) #plien de fonction pre faite
print(A.mean())
print(A.mean(axis=0))
print(A.std())#ecart type
print(A.var())#var

print("---------------------------")
print(np.corrcoef(A))
print(np.corrcoef(A)[0,1])

B = np.array([[1,2,3],[4,6,6],[1,2,3]])

print(np.corrcoef(B))

C = np.array([3,2,1,5,4])
D = np.array([2,1,0,4,3])
print(C[D])#C est reidexer

print("---------------------------")

print(np.unique(A, return_counts=True))

value, counts = np.unique(A, return_counts=True)

print(value[counts.argsort()])

for i, j in zip(value[counts.argsort()], counts[counts.argsort()]):
    print(f"la valeur {i} apparait {j}")
print("-------------Normalisation--------------")

#nan correction

#np.nanmean(a) nan not a number
#np.nanstd(A)
#np.isnpn(A) -> mask ou true = un nan trouve
#np.isnan(A).sum() -> le nombre de nan
#np.isnan(A).sum()/A.size -> pourcentage de nan dans un matrice

#correctition
#A[np.isnan(A)] = 0

np.random.seed(0)
E = np.random.randint(0,100,[10,5])
print(E)
T = E
E = E.astype(np.float64) #tip pour changer le type d'une matrice de int en float

#si je reste en int j'ai pas le possibilite d'avoir des resultat preci
print(type(E[0][0]))

print("\n")
taille = E.shape


moyenne = E.mean(axis=0)
print(moyenne)
print(type(moyenne[0]))

ecart = E.std(axis=0)
print(ecart)
print(type(ecart[0]))

for i in range(taille[1]):
    for j in range(taille[0]):
        E[j,i] = (E[j,i] - moyenne[i]) / ecart[i]

print(E)

G = (T - T.mean(axis=0)) / T.std(axis=0) #Normalisation utilisation de matrice
print("\n")
print(G)