def merge():
    b=[1, 2, 3, 4]
    c = []

    while not b:
        c.append(b[0])
        b.remove(1)
        print(b)

