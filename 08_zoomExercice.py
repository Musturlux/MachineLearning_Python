from scipy import misc
import matplotlib.pyplot as plt

face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

print(type(face))
print(face.shape)

size = face.shape
hauteur = size[0]
largueur = size[1]

print("hauteur =  {} : largueur = {} ".format(hauteur, largueur))

#ZOOOOOOM
hq = int(hauteur/8)
lq = int(largueur/8)

face = face[hq : (hauteur-hq), lq:(largueur-lq)]
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

#Mask pour la saturation
face[face > 200] = 255
face[face < 50] = 0

plt.imshow(face, cmap=plt.cm.gray)
plt.show()
   