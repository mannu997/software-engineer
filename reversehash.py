# for h= 930846109532517 answer is "lawnmower"


h = long(raw_input())
letters = "acdegilmnoprstuw"

def item ( h ):
    global letters
    string = ""
    l = len(letters)
    while(h != 7):
        for i in range(l):
            if (h-i) % 37 == 0:
                string = string + letters[i]
                h = (h-i)/37
                break
    return string[::-1]

print item( h )
    

    




