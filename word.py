import random
_word_count = 0
with open("wordlist.txt","r") as f:
    for line in f:
        _word_count += 1

def get_word():
    i = random.randint(0, _word_count - 1)
    with open("wordlist.txt","r") as f:
        for j,line in enumerate(f):
            if (j == i):
                return line.strip()