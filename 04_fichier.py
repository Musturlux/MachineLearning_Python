with open ('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {}\n".format(i, i**2))



with open ('fichier.txt', 'r') as f:
    l = []
    i = f.readline()[:-1]
    while i :
        l.append(i)
        i = f.readline()[:-1]
        
print(l)