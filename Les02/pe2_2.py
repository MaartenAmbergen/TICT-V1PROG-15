cijferICOR = float(input('Wat is je cijfer voor ICOR? '))
cijferPROG = float(input('Wat is je cijfer voor PROG? '))
cijferCSN = float(input('Wat is je cijfer voor CSN? '))
Gemiddelde = ((cijferPROG + cijferICOR + cijferCSN)/3)

print ('Mijn cijfers (gemiddeld een ' + str(round(Gemiddelde,1)) + ') leveren een beloning van € ' + str(Gemiddelde*90) + ' euro op!')