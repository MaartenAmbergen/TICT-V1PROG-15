lst= [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
aantal=0
for rij in range(len(lst)):
    for kolom in range(len(lst[0])):
        if lst[rij][kolom] >0:
            aantal += 1
print(aantal)

