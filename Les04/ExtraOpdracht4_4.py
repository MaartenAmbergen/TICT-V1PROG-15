def eindbedrag(bedrag, rentepercentage):
    nieuwbedrag=bedrag+rentepercentage*(bedrag/100)
    return(nieuwbedrag)


print(eindbedrag(eval(input('Hoe groot is je startbedrag? ')),eval(input('Hoe groot is het rentepercentage in %? '))))