def detect_palindromes(lst):
    palindromes = []
    for item in lst:
        s = str(item)  # Convert item to string
        if s == s[::-1]:
            palindromes.append(item)
    return palindromes

words = ["madam", "hello", "noon", "world", "121", "python"]
result = detect_palindromes(words)
print("Palindromes in the list:", result)