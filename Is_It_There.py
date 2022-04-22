fin = open(r"C:\Users\smlkr\Documents\Programming Documents\Python\Exercises\words.txt")

def create_dict() :
    d = dict()
    for word in fin :
        d[word.strip()] = 1
    return d

def check_in(a) :
    if a in create_dict() :
        print("yes it's in")
    else :
        print("nope")


check_in("telephone")

""" https://github.com/AllenDowney/ThinkPython2/blob/master/code/words.txt ==> You can download words.txt from here. """
