rounds, stock = input().split(" ")
rounds = int(rounds)
stock = int(stock)
sad_kids = 0
for _ in range(rounds):
    incoming = input().split(" ")
    if incoming[0] == "+":
        stock += int(incoming[1])
    elif incoming[0] == "-":
        if int(incoming[1]) > stock:
            sad_kids += 1
        else:
            stock -= int(incoming[1])
print(stock, sad_kids)