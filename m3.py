import pandas as pd
import numpy as np

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
print("----------Serie----------")
print(df["leads"])

print("----------DataFrame----------")
print(df[["leads"]])

print("----------Nom et leads----------")
print(df[["nom", "leads"]])

print("----------Tri----------")
df = df.sort_values("cout", ascending=False)
print(df)


print("----------Conditions----------")
# print(df[(df["canal"] == "Social") & (df["leads"] > 200) or (df["canal"] == "SEA")])
#print(df[(df["canal"] == "Social") & (df["leads"] > 200)])
print(df[((df["canal"] == "SEA") | (df["canal"] == "Social")) & (df["leads"] > 250)])



print("----------Index----------")
print(df.groupby("canal")[["cout","leads"]].sum().reset_index())

"""

#print(df.loc[df["canal"] == "SEA", ["nom", "cout"]])
#print(df.loc[df["cout"] > 10000, ["nom","leads"]])

#df.loc[df["canal"] == "Email", "cout"] = 1000
#print(df)

objectifs = pd.read_csv("objectifs.csv")

#print(objectifs)
#objectifs.info()

depenses = pd.read_csv("depenses.csv")
depenses["date"] = pd.to_datetime(depenses["date"])
depenses["mois"] = depenses["date"].dt.month
depenses["annee"] = depenses["date"].dt.year

print(depenses)

print("---------------------------")
print(depenses.groupby(["mois","canal"])["cout"].sum().reset_index())

sale = pd.DataFrame([
    {"canal": "  SEA  ", "cout": 1000},
    {"canal": "sea", "cout": 2000},
    {"canal": "Email ", "cout": 300},
])

print(sale.groupby("canal")["cout"].sum())

sale["canal"] = sale["canal"].str.strip().str.upper()

print(sale.groupby("canal")["cout"].sum())