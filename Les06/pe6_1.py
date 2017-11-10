def seizoen(maand):
    if maand >2 and maand <6:
        print('lente')
    elif maand >5 and maand < 9:
        print('zomer')
    elif maand > 8 and maand <12:
        print('herfst')
    elif maand >12:
        print('Je maakt een grapje!')
    elif maand <1:
        print('Je maakt een grapje!')
    else:
        print('winter')

seizoen(eval(input('maandnummer? ')))