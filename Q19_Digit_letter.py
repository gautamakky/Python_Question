chr = input("Enter a char:  ")
if chr.isdigit() or float(chr):
    print(f"{chr} is digit")
else:
    print(f"{chr} is Character")