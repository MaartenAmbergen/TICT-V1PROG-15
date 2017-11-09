Bestandsnaam='gamers.csv'
delimiter=';'

import csv

with open('gamers.csv', 'r') as myCVSFile:
    reader = csv.reader(myCVSFile, delimiter=';')
    maxscore=0
    for row in reader:
        score=int(row[2])
        if score>maxscore:
            maxscore=score
            maxnaam=row[0]
            maxdatum=row[1]
