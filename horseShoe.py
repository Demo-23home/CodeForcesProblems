colors = input().split()

uniqe = []
for color in colors:
    if color not in uniqe:
        uniqe.append(color)

print(4-len(uniqe))