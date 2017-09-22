def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = 15 + (afstandKM-50)*0.60
    elif afstandKM > 0:
        prijs = 0.80*afstandKM
    else:
        prijs = 0
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.65
        else:
            prijs = standaardprijs(afstandKM) * 0.60
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.70
        else:
            prijs = standaardprijs(afstandKM)

    return '€ ' + str(round(prijs,2))

print(ritprijs(eval(input("Hoe oud ben je? ")), eval(input("Rijs je in het weekend? (True or False) ")), eval(input("Wat is de afstand van de rit in km? "))))