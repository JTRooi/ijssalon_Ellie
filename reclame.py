from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    return str(smaak, prijs, korting)
smaak = "aardbei"
prijs = 4
korting = 0.1
prijs_na_korting = prijs * (1 - korting)
uitvoer = (f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak} , van {prijs} euro voor {prijs_na_korting} euro.")

def inkomsten_totaal(inkomsten, btw):
    return str(inkomsten, btw)
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 305]
totaal = sum(dagelijkse_inkomsten)
btw = totaal * (0.09)
uitvoer = (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    return max(), min()
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 305]
uitvoer = max(dagelijkse_inkomsten), min(dagelijkse_inkomsten)

def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len(mijn_lijst)
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 305]
gemiddelde_mijn_lijst = (sum(dagelijkse_inkomsten) / len(dagelijkse_inkomsten))
bedrag = 219.28571428571428
afgerond_bedrag = round(bedrag, 2)
uitvoer = (f"De gemiddelde inkomsten van deze week zijn {afgerond_bedrag} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
mijn_invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
uitvoer = max(mijn_invoer_lijst), min(mijn_invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print (uitvoer)