try:
    bedrag=4356
    aantal=eval(input('Hoe veel personen gaan er mee? '))
    if aantal <0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print(bedrag/aantal)

except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except NameError:
    print('Gebruik cijfers voor het invoeren van getallen!')
except:
    print('Onjuiste invoer!')
