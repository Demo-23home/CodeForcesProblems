rounds = int(input())
for i in range(rounds):
    word = input()
    if len(word) > 10:
        lenn = len(word) - 2
        strlen = str(lenn)
        output = "" + word[0] + strlen + word[-1]
    else:
        output = word
    print(output)