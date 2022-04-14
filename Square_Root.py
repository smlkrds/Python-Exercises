def Sqrt(a, x):
    n = 0
    
    while n != x :
        n = x
        x = (x + (a / x))/2

    print(x)

Sqrt(16, 6)
