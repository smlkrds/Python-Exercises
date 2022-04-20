def is_anagram(t1, t2) :
    if sorted(t1) == sorted(t2) :
        print("yes")
    else :
        print("nope")

is_anagram([1, 2, 3], [2, 3, 8, 1])
