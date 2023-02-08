def palindrome(str):
    for i in range (int((len(str))/2)):
        if str[i] != str[int(len(str)) - 1 -i]:
            return False
    return True

s = input()
if palindrome(s):
    print("This string is palindrome")
else:
    print("This string is not palindrome")