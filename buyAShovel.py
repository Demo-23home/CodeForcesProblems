k, r = map(int, input().split())
found = False
for x in range(1, 10):
    if not found:
        z = k * x
        if z % 10 == 0 or z % 10 == r:
            print(x)
            found = True
            break
