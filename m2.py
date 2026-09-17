import pandas as pd

campagnes = [
    {"nom": "Brand Search", "canal": "SEA", "cout": 12000, "leads": 480},
    {"nom": "Generic Search", "canal": "SEA", "cout": 22000, "leads": 550},
    {"nom": "Competitor Search", "canal": "SEA", "cout": 9000, "leads": 140},
    {"nom": "Display Retarget", "canal": "Display", "cout": 8000, "leads": 120},
    {"nom": "Display Prospect", "canal": "Display", "cout": 11000, "leads": 90},
    {"nom": "Newsletter", "canal": "Email", "cout": 500, "leads": 95},
    {"nom": "Email Nurturing", "canal": "Email", "cout": 800, "leads": 60},
    {"nom": "FB Prospecting", "canal": "Social", "cout": 15000, "leads": 300},
    {"nom": "IG Retarget", "canal": "Social", "cout": 6500, "leads": 210},
]

df = pd.DataFrame(campagnes)



"""
print(df)

print("--- HEAD ---")
print(df.head(2))

print("--- INFO ---")
df.info()

print("--- DESCRIBE ---")
print(df.describe())

print("--- UNE COLONNE ---")
print(df["cout"])

print("--- TYPE ---")
print(type(df["cout"]))

print("--- DEUX COLONNES ---")
print(df[["nom", "cout"]])

print("--- TYPE ---")
print(type(df[["nom", "cout"]]))

print("--- LE MASQUE ---")
print(df["cout"] > 10000)

print("--- FILTRE ---")
print(df[df["cout"] > 10000])

print("--- DEUX CONDITIONS ---")
print(df[(df["cout"] > 5000) & (df["leads"] > 200)])

print("---Exercices François---")
print(df[(df["leads"] > 100) & (df["canal"] != "SEA")])


df["cpl"] = (df["cout"] / df["leads"]).round(2)

print("--- TRI PAR CPL ---")
print(df.sort_values("cpl"))

print("--- COUT PAR CANAL ---")
print(df.groupby("canal")["cout"].sum())


print("--- PLUSIEURS COLONNES ---")
print(df.groupby("canal")[["cout", "leads"]].sum())

print("--- PLUSIEURS FONCTIONS ---")
print(df.groupby("canal").agg(
    cout_total=("cout", "sum"),
    leads_total=("leads", "sum"),
    nb_campagnes=("nom", "count"),
))
"""

resume = df.groupby("canal").agg(
    cout_total=("cout", "sum"),
    leads_total=("leads", "sum"),
).reset_index()

print("--- APRES RESET_INDEX ---")
print(resume)
print(type(resume))


objectifs = pd.DataFrame([
    {"canal": "SEA", "budget_cible": 40000},
    {"canal": "Display", "budget_cible": 25000},
    {"canal": "Email", "budget_cible": 2000},
    {"canal": "Affiliation", "budget_cible": 5000},
])

fusion = resume.merge(objectifs, on="canal", how="left")

fusion2 = resume.merge(objectifs, on="canal", how="left")

print("--- FUSION2 ---")
print(fusion2)

"""
print("--- MERGE LEFT ---")
print(fusion)

print("--- DETECTER ---")
print(fusion["budget_cible"].isna())

print("--- LIGNES SANS OBJECTIF ---")
print(fusion[fusion["budget_cible"].isna()])

print("--- REMPLACER ---")
fusion["budget_cible"] = fusion["budget_cible"].fillna(0)
print(fusion)



fusion["statut"] = np.where(fusion["cout_total"] > fusion["budget_cible"], "Dépassement", "OK")

print("--- STATUT ---")
print(fusion)
"""
import numpy as np

conditions = [
    fusion2["budget_cible"].isna(),
    fusion2["cout_total"] > fusion2["budget_cible"],
]

valeurs = ["Pas d'objectif", "Dépassement"]

fusion2["statut"] = np.select(conditions, valeurs, default="OK")

print("--- STATUT CORRIGE ---")
print(fusion2)