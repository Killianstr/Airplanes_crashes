import matplotlib.pyplot as plt
import csv
from collections import Counter
import numpy as np

#récupère l'année
def Date_rework(date_string):
    new_date = date_string[-4:]
    return new_date

#crée un histogramme et l'enregistre au format png
def Create_histo(liste_used,color,yaxe,ylab,num):
    plt.bar(list_annees,liste_used, color = color)
    plt.xlabel('Années')    
    axes.xaxis.set_ticks(np.arange(0,100,9))
    axes.yaxis.set_ticks(yaxe)
    plt.ylabel(ylab)
    plt.title(ylab + 'en fonction des années')
    plt.show()
    plt.savefig('histo'+num+'.png')

fichier = open('../Airplane_Crashes_and_Fatalities_Since_1908.csv',mode = 'r', encoding = 'utf8')
reader = csv.DictReader(fichier)

liste_dictionnaire = list(reader)

copy_csv = liste_dictionnaire[:]
list_date = []
list_annees = []
nombre_morts = []
nombre_survived = []
nombre_abord = []

#Récupère les valeurs à traiter dans des listes
for value in liste_dictionnaire:
    list_annees.append(Date_rework(value.get('Date')))
    list_date.append(value.get('Date'))
    nombre_morts.append(value.get('Fatalities'))
    nombre_survived.append(value.get('Ground'))
    nombre_abord.append(value.get('Aboard'))

dict_date = Counter(list_annees)

#Pour trouver le max et le min d'une liste
def Init_limits(l):
    value = []
    value = [min(l),max(l)]
    return value

axes = plt.gca()

#cree l'histogramme qui prend un seul paramètre 
plt.hist(list_annees,bins = 30, color = 'grey')
plt.xlabel('Années')    
axes.xaxis.set_ticks(np.arange(0,100,9))
axes.yaxis.set_ticks(np.arange(0,350,30))
plt.ylabel('Nombre de crash')
plt.title('Nombre de crash en fonction des années')
plt.show()
plt.savefig('histo1.png')

#créé les 3 autres
Create_histo(nombre_morts,'r',np.arange(0,200,30),'Nombre de morts ','2')
Create_histo(nombre_survived,'blue',np.arange(0,50,10),'Nombre de survivants ','3')
Create_histo(nombre_abord,'yellow',np.arange(0,200,30),'Nombre de personnes à bord ','4')
