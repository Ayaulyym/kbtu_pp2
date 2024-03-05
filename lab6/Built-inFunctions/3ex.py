def palindrome(s):
    s = s.replace(" " , "").lower()

    return s == s[::-1]

str = "A man a plan a canal "
if palindrome(str):
    print(f"'{str}' YES")
else:
    print(f"'{str}' NO ")
