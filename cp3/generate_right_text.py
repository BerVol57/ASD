import random

def get_random_text(n=150):
    words = []

    for _ in range(n):
        word_length = random.randint(1, 10) * 2 + 1
        word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=word_length))
        words.append(word)

    result = ' '.join(words)

    return result
