import sys

def reverse(word):
    return word[::-1]

T = int(input())

sentences = [sys.stdin.readline() for _ in range(T)]

for sentence in sentences:
    words = sentence.split()
    reversed_words = list(map(reverse, words))
    print(" ".join(reversed_words))