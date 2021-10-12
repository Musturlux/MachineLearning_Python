classeur = {
    "positif" : [],
    "négatif" : []   
    }

def trier(classeur, nombre):
    
    if nombre >= 0:
        classeur["positif"].append(nombre)
    
    else :
        classeur["négatif"].append(nombre)
    
    return classeur

trier(classeur, 3)
trier(classeur, -4)
print(classeur)