def contains(nums) :
    trial = [0,0,7, "qwerty"]
    for i in nums:
        if i == trial[0]:
            trial.pop(0)

        if len(trial) == 1:
            return True
    return False

print(contains([1, 2, 4, 0, 0, 7, 5]))
print(contains([1, 0, 2, 4, 0, 5, 7]))
print(contains([1, 7, 2, 0, 4, 5, 0])) 
