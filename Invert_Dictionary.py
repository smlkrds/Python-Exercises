def invert_dictionary(x) :
    rx = {}
    for i in x :
        rx[x.setdefault(i, 0)] = i
    print(rx)

invert_dictionary({"age": "42", "height": "186 cm", "weight(kg)": 103})
