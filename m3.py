
import pandas as pd
import numpy as np
from pathlib import Path

def charger(chemin, sep=",", encoding="utf-8", skiprows=0):
    return pd.read_csv(chemin,sep=sep,encoding=encoding,skiprows=skiprows)

def nettoyer(df, renommage, format_date):
    df = df.rename(columns=renommage)
    df = df.drop(columns="a_supprimer", errors="ignore")
    df = df[df["date"] != "TOTAL"]
    df["canal"] = df["canal"].str.strip().str.lower()
    df = df.drop_duplicates()
    df["depenses"] = df["depenses"].astype(str).str.replace(" ","").str.replace(",",".").str.replace("€","")
    df["depenses"] = pd.to_numeric(df["depenses"],errors="coerce")
    df["date"] = pd.to_datetime(df["date"],format=format_date)
    return df


RENOMMAGE_JANVIER = {"Date":"date","Canal ":"canal","Dépenses (€)":"depenses","Clics":"clics","Conversions":"conversions","Unnamed: 5":"a_supprimer"}
RENOMMAGE_FEVRIER = {"channel":"canal","spend":"depenses","clicks":"clics"}
RENOMMAGE_MARS = {"Canal": "canal", "Jour": "date", "Conversions": "conversions", "Clics": "clics", "Budget dépensé": "depenses"}

CONFIGS = {
    "export_janvier.csv": {
        "sep": ";",
        "encoding": "cp1252",
        "skiprows": 2,
        "renommage": RENOMMAGE_JANVIER,
        "format_date": "%d/%m/%Y",
    },
    "export_fevrier.csv": {
        "renommage": RENOMMAGE_FEVRIER,
        "format_date": "%Y-%m-%d",
    },
    "export_mars.csv": {
        "sep": "\t",
        "renommage": RENOMMAGE_MARS,
        "format_date": "%d/%m/%Y",
    },
    "export_avril.csv": {
    "sep": "\t",
    "renommage": RENOMMAGE_MARS,
    "format_date": "%d/%m/%Y",
    },

}

dataframes = []

for chemin in sorted(Path("donnees").glob("*.csv")):
    config = CONFIGS[chemin.name]
    df = charger(chemin, sep=config.get("sep", ","), encoding=config.get("encoding", "utf-8"), skiprows=config.get("skiprows", 0))
    df = nettoyer(df, config["renommage"], config["format_date"])
    dataframes.append(df)

total = pd.concat(dataframes, ignore_index=True)

# ===== CONSOLIDATION  =====
total["cout_par_conversion"] = (total["depenses"] / total["conversions"]).round(2)

print("----------Total----------")
print(total)



par_canal = total.groupby("canal").agg(
{"depenses": "sum", "clics": "sum", "conversions":"sum"}
).reset_index()

print("----------Canal----------")
print(par_canal)

