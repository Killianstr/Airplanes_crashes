import matplotlib.pyplot as plt
import csv
from datetime import date, time, datetime
from collections import Counter
def Date_rework(date_string):
    # new_date = date_string[-4:] + '/' + date_string[0:2] + '/' + date_string[3:5]
    new_date = date_string[-4:]
    return new_date

liste_dictionnaire = {}

fichier = open('../Airplane_Crashes_and_Fatalities_Since_1908.csv',mode = 'r', encoding = 'utf8')
liste_dictionnaire = csv.DictReader(fichier)


list_date = []
for value in liste_dictionnaire:
        list_date.append(Date_rework(value.get('Date')))

dict_date = Counter(list_date)
# dict_nbcrash = {}
# for value in list_date : 
#     if value in dict_nbcrash.keys :
#         dict_nbcrash.

def Init_limits():
    value = []
    value = [min(list_date),max(list_date)]
    # print(max(list_date))
    return value


print(liste_dictionnaire.fieldnames)
min_max = Init_limits()

plt.hist(list_date,range = (min_max[0],min_max[1]), bins = 10, color = 'grey',
            edgecolor = 'blue')
plt.xlabel('Années')
plt.ylabel('Nombre de crash')
plt.title('Nombre de crash en fonction des années')
plt.show()

#Close_csv()