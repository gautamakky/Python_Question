N = input("Enter a name: ")
vowel =""
consonant=""
vow_count =0
cons_count=0

for i in N:
    if i == 'A' or i=='a'or i == 'E' or i=='e'or i == 'I' or i=='i'or i == 'O' or i=='o'or i == 'U' or i=='u':
        vowel += i
        vow_count += 1
    else:
        consonant += i
        cons_count +=1
print(f"In {N} name, There are {vow_count} vowel which are: {vowel} and {cons_count} consonant which are: {consonant}")
