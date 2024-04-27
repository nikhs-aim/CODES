def is_vowel(c):
    return c in 'aeiouAEIOU'


input_str = "apple banana cherry orange mango"

words = input_str.split()
words.sort()

# index and element from the word list starting from 1 index
for i, word in enumerate(words, 1):
    if is_vowel(word[0]):
        print(f"{i}: {word}")
