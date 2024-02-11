n = int(input())
events = list(map(int, input().split()))

police_man = 0
untreated_crimes = 0

for index, event in enumerate(events):
    if event == -1:
        if police_man > 0:
            police_man -= 1
        else:
            untreated_crimes += 1
    else:
        police_man += event  

print(untreated_crimes)
