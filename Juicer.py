n, b, d = map(int, input().split(" "))
org_size = input().split(" ")
org_size = [int(x) for x in org_size]
sqzed = []
counter = 0
for org in org_size:
    if not org > b:
        sqzed.append(org)
        total_sum = sum(sqzed)
        if total_sum > d:
            sqzed.clear()
            counter += 1
print(counter)

