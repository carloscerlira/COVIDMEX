import numpy as np 
import pandas as pd 
import geopandas as gdp
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

# link = 'https://en.wikipedia.org/wiki/List_of_Mexican_states_by_population'

# tables = pd.read_html(link,header=1, index_col=0)
# table = tables[0]
# table = table[['State', 'Population (2015)[2]']]
# table = table.rename(columns={'Population (2015)[2]':'Población','State':'Estado'})
# table['Estado'] = table['Estado'].str.upper()
# table = table.set_index('Estado')
# table = table.sort_index()
# population = table['Población'] 
# population = population.rename(index={'COAHUILA DE ZARAGOZA':'COAHUILA', 'QUERÉTARO DE ARTEAGA':'QUERETARO'})
# population = population.drop('TOTAL')
# population['NACIONAL'] = population.sum()
# print(population)
# population.to_csv('data/population_MX.csv')

index = ['MÉXICO', 'CIUDAD DE MÉXICO', 'CUERNAVACA']
T = [20,25,30]
P = [1,1.5]
a = pd.DataFrame(T, index=index, columns=['TEMPERATURA'])
b = pd.DataFrame(P, index=index[:-1], columns=['PRESIÓN'])
a['PRESIÓN'] = b['PRESIÓN']
print(a)