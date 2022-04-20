def has_duplicates() :
    t = [1, 2, 3, 4, 5, 6, 6]

    for i in t :
        if t.count(i) > 1 :
            print("True")
        else :
            print("False")

has_duplicates()
