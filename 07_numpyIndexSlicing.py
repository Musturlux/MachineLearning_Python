import numpy as np

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(A[0,0])

print(A[2,1])

#A[debut:fin ligne, debut:fin colone]

print(A[:,0]) #Prmeiere colone
print(A[0]) #Premiere ligne

print(A[0:2, 0:2])

B = A[0:2, 0:2] #sous tableau

#rewrite A
A[0:2, 0:2]  =10
print(A) 
print("------------------------")
print(A[:, -2:])
print("------------------------")

B = np.zeros((4,4))

print(B)
B[1:3,1:3] = 1
print("\n")
print(B)

print("------------------------")

C = np.zeros((6,6))
C[::2, ::2]  =1
print(C)

print("------------------------")

D  = np.random.randint(0,10,[5,5])
print(D < 6) #mask
print("\n")
D[D<6] = 10
print(D)

print("------------------------")
D  = np.random.randint(0,10,[5,5])
D[(D<6) & (D>2)] = 10
print(D)

print("------------------------")
#Boolean Indexing selection mask 
#Le mask E selection les valeur de F
E = np.random.randint(0,10, [5,5])
print("E : ")
print(E)

F = np.random.randn(5,5)
print("F : ")
print(F)

print("On ne garde les valeu de F que su mask de E pou les valeur > 5")
print(F[E>5])
print("Le resultat est un tableau à une dimansion")
