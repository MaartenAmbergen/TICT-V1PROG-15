def eindbedrag():
    nieuwbedrag=bedrag+rentepercentage*(bedrag/100)
    print(nieuwbedrag)

bedrag=eval(input('Hoe groot is je startbedrag? '))
rentepercentage=eval(input('Hoe groot is het rentepercentage in %? '))
eindbedrag()