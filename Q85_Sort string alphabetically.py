def sort_string_alphabetically(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chars[j] > chars[j + 1]:
                # Swap
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)

s = input("Enter string: ")
result = sort_string_alphabetically(s)
print("Sorted string:", result)