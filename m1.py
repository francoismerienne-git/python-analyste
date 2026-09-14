
def cout_par_conversion(budget, conversions):
    return budget/conversions

def alerte(cout):
    if cout > 50:
        return "ALERTE"
    else:
        return "SAFE"

campagnes = [
    {"nom":"campagne1", "budget":1000,"conversions":50},
    {"nom":"campagne2", "budget":2000,"conversions":50},
    {"nom":"campagne3", "budget":10000,"conversions":100},
    {"nom":"campagne4", "budget":20000,"conversions":1000}
]

for ligne in campagnes:
    cout = cout_par_conversion(ligne["budget"],ligne["conversions"])
    print(ligne["nom"], cout,alerte(cout))
    