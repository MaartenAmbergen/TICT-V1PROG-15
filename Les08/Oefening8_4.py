string=input('Voer een string in: ')
for letters in string:
    waarde = ord(letters)
    print('{} {} {:x} {:b}'.format(letters,waarde, waarde, waarde))
