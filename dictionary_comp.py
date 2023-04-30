from pprint import pprint

sentence = "This is very common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency)
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1], reverse=True)
pprint(char_frequency_sorted[0])
