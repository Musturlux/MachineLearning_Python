import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("titanic3.xls")

print(data.columns)
print(data.head())

#Elimine les info pas tres utile dans notre cas

data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

print(data.describe())

#MANQUE DES DONNE SUR AGE vu grace a la difference entre les place et les age

#data.fillna(data['age'].mean()) on rempli les cases manquantes par age moyen

#Ici on prefera perdre quenlque ligne
data = data.dropna(axis = 0)
print("-----------------------------------------------------")
print(data.describe())
print("-----------------------------------------------------")

print(data['pclass'].value_counts())

#data['pclass'].value_counts().plot.bar()
data['age'].hist()

print(data.groupby(['sex', 'pclass']).mean())

print("Que les mineurs")
print(data[data['age'] < 18].groupby(['sex', 'pclass']).mean())

#index comme numpy data.iloc[0,1] data.iloc[0:2, 0:2]
#data.loc pour les colonnes