string = input()

result = 0
start = ord("a")
for i in range(len(string)):
    distance = (ord(string[i]) - start) % 26
    if distance < 0:
        distance += 26
    result += min(distance, 26 - distance)
    start = ord(string[i])

print(result)