import pandas as pd
import numpy as np

#Charger depenses.csv
depenses = pd.read_csv("depenses.csv")


#Convertir la colonne date, en extraire le mois
depenses["date"] = pd.to_datetime(depenses["date"])
depenses["mois"] = depenses["date"].dt.month

#Nettoyer la colonne canal (espaces + casse)
depenses["canal"] = depenses["canal"].str.strip().str.upper()


#agréger le coût total par canal, avec canal en colonne. Range le résultat dans une variable
cout_total = depenses.groupby(["canal"])["cout"].sum().reset_index()
#print("--------------Table cout total--------------")
#print(cout_total)

#Joindre objectifs.csv en gardant tous les canaux dépensiers
objectifs = pd.read_csv("objectifs.csv")

objectifs["canal"] = objectifs["canal"].str.strip().str.upper()

fusion = cout_total.merge(objectifs, on="canal", how="left")


#Créer une colonne ecart = coût total moins budget
fusion["ecarts"] = fusion["cout"] - fusion["budget"]


#Créer une colonne statut : « Pas d'objectif » si le budget est manquant, « Dépassement » si l'écart est positif, « OK » sinon
conditions = [
    fusion["budget"].isna(),
    fusion["ecarts"] > 0,
]

valeurs = ["Pas d'objectif", "Dépassement"]

fusion["statut"] = np.select(conditions, valeurs, default="OK")

#Trier par coût total décroissant et afficher
print(fusion.sort_values("cout", ascending=False))