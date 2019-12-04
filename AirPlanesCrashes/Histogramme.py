import matplotlib.pyplot as plt
import csv

liste_dictionnaire = {}

fichier = open('../Airplane_Crashes_and_Fatalities_Since_1908.csv',mode = 'r', encoding = 'utf8')
liste_dictionnaire = csv.DictReader(fichier)
       

def Init_limits():
    # for value in liste_dictionnaire["Date"]:
    #     date_min = min(value)
    # print(date_min)
    for row in liste_dictionnaire:
        print(row)


def Close_csv():
    fichier.close()

print(liste_dictionnaire)
for row in liste_dictionnaire:
        print(row)

#Close_csv()