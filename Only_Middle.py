def only_middle() :
    t = [1, 2, 3, 4, 5, 6]
    del(t[-1])
    del(t[0])
    print(t)

only_middle()
