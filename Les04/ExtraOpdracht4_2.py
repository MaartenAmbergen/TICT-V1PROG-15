def Geefmelding(Temp):
    if Temp <= 15 and Temp >= 0:
        return('Het is koud vandaag!')
    elif Temp < 0:
        return('Het vriest!')
    else:
        return('Het is lekker weer vandaag!')
print(Geefmelding(eval(input('Hoe warm is het vandaag? '))))