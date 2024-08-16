

letters = input()
new_letters = letters[1:-1]
clean_letters = new_letters.strip()
list_letters = clean_letters.split(',')
new_list_letters = []
for list_letter in list_letters:
    letter = list_letter.strip()
    new_list_letters.append(letter)
uniqe_letters = set(new_list_letters)
counter = 0
for uniqe_letter in uniqe_letters:
    if uniqe_letter == "":
        pass
    else:
        counter += 1
print(counter)