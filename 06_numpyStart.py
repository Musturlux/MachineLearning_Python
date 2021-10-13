import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)

b = np.zeros((3, 2))
print(b)

c = np.ones((3,4))
print(c)
print(c.size)

np.random.seed(9030)

d = np.random.randn(2,4)
print(d)

e = np.eye(4)
print(e)

f = np.linspace(0, 10, 20, dtype=np.float16())
print(f)

g = np.arange(0,10, 1)
print(g)

A = np.zeros((3,2))
B = np.ones((3,2))

##Manip

print("------------------------")

C = np.hstack((A,B))
print(C)

D = np.vstack((A,B))
print(D)

C = np.concatenate((A,B), axis=1)
print(C)

D = np.concatenate((A,B), axis=0)
print(D)

print("------------------------")

D = D.reshape((3,4))
print(D)

print("Modif du shape pour 1 dim\n")

E = np.array([1,2,3])
E = E.reshape((A.shape[0], 1))
print(E.shape)

E = E.squeeze()#suprime les 1 des shape
print(E.shape)

print(D.ravel())

print("------------------------")

def initMatric(m,n):
    R = np.random.randn(m,n)
    R = np.concatenate((R,np.ones((m,1))), axis = 1)
    print(R)
    return R

initMatric(7, 4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    