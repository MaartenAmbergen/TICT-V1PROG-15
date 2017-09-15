list=[4,0,1,-2]

def swap(list):
    if len(list)>1:
        list[0], list[1]=list[1], list[0]
        return list
    