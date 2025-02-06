def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

gram_value = 100
ounce_value = grams_to_ounces(gram_value)
print(f"{gram_value} grams is equal to {ounce_value:.2f} ounces")
