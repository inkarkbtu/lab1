from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)