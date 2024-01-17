word_list = ['hello', 'world', 'name', 'python', 'programming']
n = 4
longer_words = []
for word in word_list:
    if len(word) > n:
        longer_words.append(word)
print(longer_words)
