def vowel_count(n):
    vowel =0
    cons = 0
    for i in n:
        if i.isalpha():
            if i == 'A' or i == 'a' or i == 'E' or i == 'e'or i == 'i'or i == 'I'or i == 'O'or i == 'o'or i == 'U'or i == 'u':
                vowel += 1
            else:
                cons += 1
    return print(f"There are {vowel} vowels and {cons} cons in the string.")


n = input("Enter the string: ")
vowel_count(n)
