import math

def hypotenuse():
    """ leg_a_to_b : One of the short leg of our triangle.
        leg_b_to_c : One of the short leg of our triangle.
        Hypotenuse formula : a^2 + b^2 = c^2 """
        
    leg_a_to_b = int(input())
    leg_b_to_c = int(input())
    Hypotenuse = math.sqrt(leg_a_to_b**2 + leg_b_to_c**2)

    print(int(Hypotenuse))

hypotenuse()
