import glob

with open ('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {}\n".format(i, i**2))
    
with open ('fichier1.txt', 'w') as f:
    f.write("Jean\n")
    f.write("Pierre\n")
    f.write("Paul\n")
    f.write("Jaque\n")

dico = {}
l = []
filenames = glob.glob("*.txt")

for file in filenames:
    l = [line.strip() for line in open(file, 'r')]
    dico[file] = l
    #dico[file] = f.read().splitlines()

print(dico)