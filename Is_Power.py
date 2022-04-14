def is_power(x, y):
    if x == y:
        return True
    elif x % y == 0 and is_power((int(x / y)), y) == True :
        return True
    else: 
        return False

print(is_power(125, 5))

""" We are checking if x is a power of y. """
