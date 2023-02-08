def convert_grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

g = int(input())
print(convert_grams_to_ounces(g))