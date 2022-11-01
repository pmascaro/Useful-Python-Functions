#-----------
#
# Import required libraries
# 
#-----------
import numpy as np
import pandas as pd

# to generate random numbers
import random

#-----------
#
# Create empty dataframe from scratch and storing it in variable df
#
#-----------
df = pd.DataFrame()

# create a list for each column
name = ['Toni','Joanmi','Biel','Pere','Xisco','Xavi','Miquel','Jordi','Toni']
surname = ['Rigo','Perello','Nadal','Manresa','Adrover','Coves','Caldentey','Bauza','Mestre']
hobby = ['Running', 'Triathlon','Crossfit', 'Bouldering', 'Yoga', 'Running', 'Crossfit', 'Sailing']
city_residence = ['Felanitx', 'Palma', 'Barcelona', 'Barcelona', 'Portocolom', 'Eivissa', 'Felanitx', 'Felanitx']
country_residence = ['Spain', 'Spain', 'Spain', 'Spain', 'Spain', 'Spain', 'Spain', 'Spain']
no_cousins = [13, 13, 11, 12, 12, 14, 15, 11, 4]

# list of column names
columns=['name','surname',hobby,city_residence,country_residence,no_cousins]

df = pd.DataFrame( ,columns = columns)