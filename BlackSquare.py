cal = list(map(int, input().split()))
repeats = input()

# print(cal, repeats)


loss1 = int(repeats.count('1')) * cal[0]
loss2 = int(repeats.count('2')) * cal[1]
loss3 = int(repeats.count('3')) * cal[2]
loss4 = int(repeats.count('4')) * cal[3]

total_loss = loss1 + loss2 + loss3 + loss4

print(total_loss)