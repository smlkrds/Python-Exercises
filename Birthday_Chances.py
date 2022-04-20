import random

def birthday_chances() :
    t = [random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), 
    random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), 
    random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), random.randint(0, 366),
    random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), random.randint(0, 366),
    random.randint(0, 366), random.randint(0, 366), random.randint(0, 366), random.randint(0, 366),
    random.randint(0, 366), random.randint(0, 366), random.randint(0, 366)]
    pb = 0

    for i in t :
        for j in range(24) :
            if t[j - 1] == i :
                pb += 1
    print((pb-23) / 46)
    print(sorted(t))


birthday_chances()
