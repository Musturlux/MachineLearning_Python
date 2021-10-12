def fibo (n) :
    suivant = 1
    current = 0
    while n >= current :
        print(current)
        tmp = suivant
        suivant = suivant + current
        current = tmp
        
def bestFibo(n):
    a = 0
    b = 1
    while a < n:
        print(a)
        a, b = b, a+b
    
fibo (132)
bestFibo(1000)

def fiboListe(n):
    a = 0
    b = 1
    l =[]
    while a < n:
        l.append(a)
        a, b = b, a+b
    print(l)
    return l

fiboListe(1000)