def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for c in text:
        if c.lower() in vowels:
            count += 1
    return count

    # return sum([1 for c in text if c.lower() in volwels])

