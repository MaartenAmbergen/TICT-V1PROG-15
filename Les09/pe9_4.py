import csv
with open('producten.csv', 'w', newline='')as myCSVFile:
    writer=csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('1 ')
        if artikelnummer=='einde':
            break

        artikelcode = input('2 ')
        if artikelcode=='einde':
            break

        naam = input('3 ')
        if naam=='einde':
            break
        vorraad = input('4 ')
        if vorraad=='einde':
            break

        prijs = input('5 ')
        if prijs=='einde':
            break