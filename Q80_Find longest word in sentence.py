
n = input("Enter the sentence: ").split()
max_word = n[0]

for word in n[1:]:
    if len(word) > len(max_word):
        max_word = word

print(f"The longest word is: {max_word}")