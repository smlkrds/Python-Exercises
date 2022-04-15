import math

def calculate_pi():
    epsilon = 10 ** (-7)
    Pi = 3.14
    t = 0
    while math.sqrt((Pi - math.pi) ** 2) > epsilon :
        k = 0
        y = (math.factorial(4 * k) * (1103 + (26390 * k))) / (math.factorial(k) ** 4) * (396 ** (4 * k))
        t += y
        x = ((2 * math.sqrt(2)) / 9801) * t
        Pi = 1 / x
        k += 1
        print ("{0:.6f}".format(Pi))

calculate_pi()
