def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    print(d)

histogram("education")
