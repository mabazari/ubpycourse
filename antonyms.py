antonym=dict()    
while True:
    w1 = input("pleas enter a word=")
    w1 = w1.lower()

    if w1 in antonym.keys():
        print(antonym[w1])

    elif w1 in antonym.values():
        for word,aword in antonym.items():
            if aword==w1:
                print(word)
    else:
        print("i dont know antonym of",w1)
        b = input("do you know?(yes=y/no=n)")
        b = b.lower()
        if b == 'y':
            w2 = input('what is it?')
            w2 = w2.lower()
            antonym[w1] = w2
            q=u'Thanks \u2713'
            print(q)
