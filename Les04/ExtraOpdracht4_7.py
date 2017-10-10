def berekensomevengetallen(getallenrij):
    x=0
    for getal in getallenrij:
        if getal%2==0:
            x=x+getal
    return(x)
def berekensomonevengetallen(getallenrij):
    y=0
    for getal in getallenrij:
        if getal%2==1:
            y=y+getal
    return(y)

getallenrij=[23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
print('de som van de even getallen bedraagt {}'.format(berekensomevengetallen(getallenrij)))
print('de som van de oneven getallen bedraagt {}'.format(berekensomonevengetallen(getallenrij)))