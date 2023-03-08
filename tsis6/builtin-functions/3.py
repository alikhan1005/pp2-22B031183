def palindrome(str):
    l = len(str)
    if l == 1:
        return True
    
    for i in range(0,int(l/2)):
        if str[i] != str[l-1-i]:
            return False
    return True

str = input()
print(palindrome(str))