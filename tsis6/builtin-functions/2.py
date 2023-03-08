def upper_lower(str):
    u = 0
    l = 0

    for i in str:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1

    return(u, l)

str = input()
number = upper_lower(str)
print(number)