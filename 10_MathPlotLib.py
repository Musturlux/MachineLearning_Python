import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 10)
y = x**2

#plt.plot(x,y)
#plt.show()
#Attention au dimention !!

#Param c coleur c='red'
#Param lw line wight epaisseur du trait lw=5
#Param ls line style ls='--'

#=====================================

plt.figure()#feuille de travaille
#param figsize (en inch) pour demensionner le taille de la figure


plt.plot(x, y, label="quadratique")#on dessine sur le figure
plt.plot(x, x**3, label="cubique")
plt.title("TestMathPlot")
plt.xlabel("axe x")
plt.ylabel("axe y")
plt.legend()
plt.show()

plt.savefig('TestMathPlot.png')

#====================================

plt.subplot(2, 1, 1)
plt.plot(x, y, c='red')

plt.subplot(2, 1, 2)
plt.plot(x, y, c='blue')

#===================================
dataset = {f"experience{i}": np.random.randn(100) for i in range (4)}
#On se cree un dico de data avec 4 entre

# print(dataset)

def graphique(dataset):
    
    lkey = list(dataset.keys())
    plt.figure()
    
    for i in range(len(lkey)):
        plt.subplot(len(lkey), 1, i+1)
        plt.plot(dataset.get(lkey[i]))
    
    plt.show()
    
graphique(dataset)