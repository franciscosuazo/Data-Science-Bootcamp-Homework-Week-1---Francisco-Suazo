def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for varchar in word:
        if varchar in vowels:
            count += 1
    return count

result = count_vowels("Bootcamp")
print(result)

