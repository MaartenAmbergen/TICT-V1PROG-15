bruin=set(["Boxtel", "Best", 27,  "Eindhoven", "Helmond 't hout", "Helmond", "Helmond Brouwhuis", "Deurne"])
groen=set(["Boxtel", 24, "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", 25, "Weert"] )

print("De volgende plaatsen worden in beide routes aangedaan: ")
print(set.intersection(bruin, groen))

print("De volgende plaatsen worden niet in beide routes aangedaan:")
print(set.difference(bruin, groen))

print("de bruine lijn doet de volgende stations aan:")
print(set(bruin))

print("de groene lijn doet de volgende stations aan:")
print(set(groen))
