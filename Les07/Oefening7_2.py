week={'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do':'donderdag', 'vr': 'vrijdag'}

print(week)\

print('ma' in week)

print(week['ma'])

week['di']='dinsdag'
print(week)

week['za']='zaterdag'
print(week)

for afkorting in week.keys():
    print(afkorting)

for langenaam in week.values():
    print(langenaam)

for beiden in week.items():
    print(beiden)
for afkorting in week:
    print('afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))