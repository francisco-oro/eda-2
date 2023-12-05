"""
    Francisco Oro @ FI UNAM
    Estructura de Datos y Algoritmos II
    Examen Parcial 3
    Problema 1
"""

import re


def longest_words(line: list) -> dict:
    line.sort(key=len, reverse=True)
    longest_length = len(line[0])
    # List comprehension to store de word and number of instances of that word
    counts = [(word, line.count(word)) for word in line if len(word) == longest_length]
    return dict(counts)


# Function that takes in the text and a tuple of delimiters to split that text into a list of words
def split_words(string: str, delimiters: tuple) -> list:
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, string)

if __name__ == '__main__':
    file = open("AlanTuring.txt", mode='r', encoding='utf-8')
    text = file.read().lower()

    words = SplitWords(text, delimiters=(",", ";", '\n', '\t', '-', " "))
    print(f"Longest words found : {LongestWords(words)}")
    file.close()
