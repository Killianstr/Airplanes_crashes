import folium
import pandas as pd
import csv
import json


liste_dictionnaire = {}

center = (50,20)
map = folium.Map(location=center, tiles='OpenStreetMap', zoom_start=3)

fichier = open('../Airplane_Crashes_and_Fatalities_Since_1908.csv',mode = 'r', encoding = 'utf8')
liste_dictionnaire = csv.DictReader(fichier)

fichier_countries = open('../Countries.csv',mode = 'r', encoding = 'utf8')
liste_countries = csv.DictReader(fichier_countries)


#Add Country in liste_dictionnaire
for value in liste_dictionnaire :
    loc = value.get('Location')
    loc_split = loc.split(', ')
    value['Country'] = loc_split[len(loc_split)-1]
    for value2 in liste_countries :
        if loc_split[len(loc_split)-1] == value2.get('Location')
    #print(value.get('Country'))


#Add id Country in liste_dictionnaire
for value in liste_dictionnaire :
    count = value.get('Country')
    value['id'] = 
    #print(value.get('Country'))





country_geo = json.load(open("country.geojson"))
state_data = pd.read_csv(fichier)

map.choropleth(
 geo_data=country_geo,
 name='choropleth',
 data=listes_dictionnaire,
 columns=['Country', 'Fatalities'],
 key_on='feature.id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Fatalities'
)
folium.LayerControl().add_to(map)

map.save(outfile='map.html')