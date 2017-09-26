lengte=eval(input('Hoe lang ben je? (in meters)'))
gewicht=eval(input('Hoe veel weeg je? (in kg)'))
BMI=gewicht/(lengte**2)
print('Je BMI is {}'.format(BMI))

if BMI <= 18.8:
    print('ondergewicht')
elif (BMI > 18.5) and (BMI <= 25):
    print('Normaal')
else:
    print('Overgewicht')