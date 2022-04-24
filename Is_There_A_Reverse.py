fin = open(r"C:\Users\smlkr\Documents\Programming Documents\Python\Exercises\words.txt")

def find_rotate_pairs() :
    d = dict()
    for word in fin :
        a = word.strip()
        d[a] = d.setdefault(a, 0)
    for i in d :
        if i[::-1] in d :
            print(i, i[::-1])

print(find_rotate_pairs())

""" 
