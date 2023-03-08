def all_elements_true(x):
    return all(x)

tuple = (True, True, False, False, True, False, True)
if all_elements_true(tuple):
    print(" all elements of the tuple are true")
else:
    print(" all elements of the tuple are false")