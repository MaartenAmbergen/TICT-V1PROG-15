def berekensomevengetallen(getallenrij):
    x=0
    for getal in getallenrij:
        if getal%2==0:
            x=x+getal
    return(x)

getallenrij=[23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
print('de som van de even getallen bedraagt {}'.format(berekensomevengetallen(getallenrij)))