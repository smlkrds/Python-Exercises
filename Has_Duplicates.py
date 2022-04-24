def has_duplicates() :
    t = [1, 2, 3, 4, 5, 6, 6]

    for i in t :
        if t.count(i) > 1 :
            print("True")
        else :
            print("False")

has_duplicates()


""" Or

def has_duplicates() :
    t = [1, 2, 3, 4, 5, 6]
    d = dict()
    for i in t :
        d[i] = d.setdefault(i, 0)
        d[i] += 1
        if d.setdefault(i, 1) > 1 :
            return "it has duplicate!"
    return "nope"
    
print(has_duplicates()) ==> This is same thing but made with dictionary. """
