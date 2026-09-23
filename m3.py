# ===== JANVIER =====

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



#Index(['Date', 'Canal ', 'Dépenses (€)', 'Clics', 'Conversions'], dtype='str')


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

#Export to clean csv
janvier.to_csv("sorties/janvier_propre.csv",index=False)



# ===== FEVRIER =====

fevrier = pd.read_csv("donnees/export_fevrier.csv",sep=",")

#From english to french
fevrier = fevrier.rename(columns={"channel":"canal","spend":"depenses","clicks":"clics"})

#Lower case
fevrier["canal"] = fevrier["canal"].str.lower().str.strip()

#Deduplicate
fevrier = fevrier.drop_duplicates()

#Clean date format
fevrier["date"] = pd.to_datetime(fevrier["date"],format="%Y-%m-%d")

#Export to clean csv
fevrier.to_csv("sorties/fevrier_propre.csv",index=False)
""


# ===== MARS =====

mars = pd.read_csv("donnees/export_mars.csv",sep="\t")

#Rename columns
mars = mars.rename(columns={"Canal":"canal","Jour":"date","Conversions":"conversions","Clics":"clics","Budget dépensé":"depenses"})

#Clean canal with lower case and spaces
mars["canal"] = mars["canal"].str.lower().str.strip()

#clean depenses
mars["depenses"] = mars["depenses"].str.replace(" ","").str.replace(",",".").str.replace("€","")

#Deduplicate
mars = mars.drop_duplicates()

#Depenses from string to float
mars["depenses"] = pd.to_numeric(mars["depenses"],errors="coerce")

#Clean date format
mars["date"] = pd.to_datetime(mars["date"],format="%d/%m/%Y")

#Export to clean csv
mars.to_csv("sorties/mars_propre.csv",index=False)

"""
print("----------Mars Cleané----------")
print(mars)

print("----------Mars Info----------")
mars.info()
"""


# ===== CONSOLIDATION  =====


total = pd.concat([janvier,fevrier,mars],ignore_index=True)
print("----------Total----------")
print(total)
#total.info()
#print(total["canal"].value_counts())

total["cout_par_conversion"] = (total["depenses"] / total["conversions"]).round(2)


par_canal = total.groupby("canal").agg(
{"depenses": "sum", "clics": "sum", "conversions":"sum"}
).reset_index()

print(par_canal)
