import numpy as np
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

yestersay = '4/8/20'
today = '4/9/20'

confirmedraw = pd.read_csv('data/covidmxraw.csv', skiprows=3, index_col=0)
confirmedraw = confirmedraw.dropna()
confirmedraw = confirmedraw[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
confirmedraw = confirmedraw.rename(columns={'Unnamed: 1':'Estado', 'Unnamed: 2':'Sexo', 'Unnamed: 3':'Edad'})
confirmedraw['Estado'] = confirmedraw['Estado'].apply(lambda name: name[:-1])
confirmedraw.to_csv('data/confirmedraw.csv')

confirmed = pd.read_csv('data/time_series_confirmed_MX.csv', index_col=0)
current = confirmedraw.groupby('Estado')['Sexo'].count()
last = confirmed[yestersay]

confirmed[today] = last + (current-last)
confirmed[today][-1] = current.sum()
confirmed.to_csv('data/time_series_confirmed_MX.csv')

deaths = pd.read_csv('data/time_series_deaths_MX.csv', index_col=0)
deathsraw = pd.read_csv('data/deathsraw.csv')
new = deathsraw.groupby('ObservationDay').get_group(today)
new = new.set_index('Estado')['Deaths']
deaths[today] = new
deaths[today][-1] = new.sum()
deaths = deaths.fillna(0)
deaths.to_csv('data/time_series_deaths_MX.csv')

states = gpd.read_file('data/geopandas/states.shp')
infected = confirmed[today][:-1]
infected = infected.rename({'CIUDAD DE MÉXICO': 'DISTRITO FEDERAL', 'MÉXICO': 'MEXICO', 'NUEVO LEÓN':'NUEVO LEON', 'SAN LUIS POTOSÍ':'SAN LUIS POTOSI'})
infected = infected.sort_index()
states['infected'] = infected.values
states.to_file('data/geopandas/states.shp')

# path = 'data/geopandas/PHLITL_2000.shp'
# data = gpd.read_file(path)
# counties = data[['EDO_LEY', 'geometry']]
# states = counties.dissolve(by='EDO_LEY')
# states = states.sort_index()
# states 
# print(states)