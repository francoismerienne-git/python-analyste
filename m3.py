import pandas as pd
import numpy as np

#import + encoding + séparateur + skpi rows
janvier = pd.read_csv("donnees/export_janvier.csv",encoding="cp1252",sep=";",skiprows=2)

#drop colonne fantome
janvier = janvier.drop(columns="Unnamed: 5")

#enlever ligne total
janvier = janvier[janvier["Date"] != "TOTAL"]

#janvier.info()


#print(janvier.duplicated().sum())
#print(janvier[janvier.duplicated(keep=False)])

#enlever doublons
janvier = janvier.drop_duplicates()

#vérifier que les doublons ont disparu
#print(janvier.duplicated().sum())


"""
Index(['Date', 'Canal ', 'Dépenses (€)', 'Clics', 'Conversions'], dtype='str')
"""

#Rename columns
janvier = janvier.rename(columns={"Date":"date","Canal ":"canal","Dépenses (€)":"depenses","Clics":"clics","Conversions":"conversions"})

#Clean canal : lower & remove space
janvier["canal"] = janvier["canal"].str.strip().str.lower()
#print(janvier["canal"].unique())


#Clean depenses : from french to english format
janvier["depenses"] = janvier["depenses"].str.replace(" ","").str.replace(",",".")

#Depenses from string to float
janvier["depenses"] = pd.to_numeric(janvier["depenses"],errors="coerce")

#Clean date format
janvier["date"] = pd.to_datetime(janvier["date"],format="%d/%m/%Y")

print(janvier.isna())
print(janvier.isna().sum())