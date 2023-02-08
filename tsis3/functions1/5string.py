def permutations(string):
    if len(string) == 0:
        return ['']
    before_list = permutations(string[1:len(string)])
    next_list = []
    for i in range (len(before_list)):
        for j in range (len(string)):
            new_str = before_list[i][0:j] + string[0] + before_list[i][j:len(string) - 1]
        
            if new_str not in next_list:
                next_list.append(new_str)

    return next_list

s = input()
print(permutations(s))