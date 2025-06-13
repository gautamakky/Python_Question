n = input("Enter sentence: ").split()
min_word = n[0]
for i in n:
    if len(i) < len(min_word):
        min_word = i
print("sortest length is: ",min_word)
