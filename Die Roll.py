from fractions import Fraction
y, w = map(int, input().split())

min_val = max(y, w)
counter = 0
for i in range(1, 7):
    if i >= min_val:
        counter += 1

f = Fraction(counter, 6)
if f == 0:
    f = "0/1"
elif f == 1:
    f = "1/1"

print(f)
