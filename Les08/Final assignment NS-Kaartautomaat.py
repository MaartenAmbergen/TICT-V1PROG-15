def inlezen_beginstation(stations):
    beginstation = input('Geef begin station: ')
    while beginstation not in stations:
        beginstation = input('Niet goed, geef beginstation')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Geef eind station: ')
    while eindstation not in stations:
        eindstation = input('Niet goed, geef eindstation')
    while stations.index(eindstation)< stations.index(beginstation):
        eindstation = input('Niet goed, geef eindstation')
    return eindstation

# def omroepen_reis(stations, beginstation, eindstation):
#     nummerB = stations.index(beginstation) +1
#     nummerE = stations.index(eindstation) +1
#     huidig_station = stations.index(beginstation) +1
#     print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, nummerB))
#     print('Het eindstation {} is het {}e station in het traject'.format(eindstation, nummerE))
#     print('de afstand bedraagt {} stations'.format(nummerE-nummerB))
#     print('De prijs van je rijs is {} euro'.format((nummerE-nummerB)*5))
#     print('je stapt in de trein in: {}'.format(beginstation))
#     while huidig_station < stations.index(eindstation):
#         print('- {}'.format(huidig_station))
#         huidig_station = huidig_station + 1
#     print('je stapt uit de trein in : {}'.format(eindstation))

def omroepen_reis(stations,beginstation,eindstation):
    beginstationIndex = stations.index(beginstation)
    eindstationIndex = stations.index(eindstation)
    verschil = eindstationIndex - beginstationIndex
    ritprijs = verschil * 5
    tussenstations = ""
    print(beginstation, beginstationIndex)
    print(eindstation, eindstationIndex)
    print("de afstand is ",verschil)
    print("je ritprijs is ",ritprijs)
    for i in range(beginstationIndex, eindstationIndex):

        tussenstations += stations[i] + "\n "
    # goedetussenstations = tussenstations - beginstation
    print("je reis begint in", beginstation, "en je tussnestations zijn",tussenstations,"je eindigt in", eindstation )


stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal','Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosh','Eindhoven','Weert','Roermond','Sittard', 'Maastricht']
beginstation= inlezen_beginstation(stations)
eindstation= inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)