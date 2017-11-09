import random

def monopolyworp():
    worp1=random.randrange(1, 7)
    worp2=random.randrange(1, 7)
    if worp1==worp2:
        print("{} + {} = {} (dubbel)".format(worp1, worp2, (worp1+worp2)))
        worp3 = random.randrange(1, 7)
        worp4 = random.randrange(1, 7)
        if worp3 == worp4:
            print("{} + {} = {} (dubbel)".format(worp1, worp2, (worp3 + worp4)))
            worp5 = random.randrange(1, 7)
            worp6 = random.randrange(1, 7)
            if worp5==worp6:
                print("{} + {} = {} (Direct naar de gevangenis!)".format(worp5, worp6, (worp5 + worp6)))
            else:
                print("{} + {} = {}".format(worp5, worp6, (worp5 + worp6)))
        else:
            print("{} + {} = {}".format(worp3, worp4, (worp3 + worp4)))
    else:
        print("{} + {} = {}".format(worp1, worp2, (worp1+worp2)))

monopolyworp()