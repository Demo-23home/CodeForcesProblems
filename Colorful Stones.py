s = list(input())
t = list(input())
liss_pos = 0
for i in range( len(t) ):
    if t[i] == s[liss_pos]:
        liss_pos += 1

print(liss_pos+1)
