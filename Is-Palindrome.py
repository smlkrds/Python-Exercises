def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if first(word) == last(word) and middle(word) == middle(word[::-1]):
        print("yes")
    else:
        print("no")

is_palindrome("palindrome")
