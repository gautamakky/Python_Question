# Q(6) # Marks & Subject Eligibility Checker
# Problem:
#
# You have 3 subjects. To pass:
#
# Each subject must have ≥ 40
#
# Average must be ≥ 50
#
m1 = int(input("Math: "))
m2 = int(input("Science: "))
m3 = int(input("English: "))

average = (m1 + m2 + m3) / 3

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    if average >= 50:
        print("Passed with average:", average)
    else:
        print("Failed due to low average")
else:
    print("Failed in one or more subjects")