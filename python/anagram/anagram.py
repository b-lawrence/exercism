from collections import Counter


def is_anagram(base_word, comparator):
    return Counter(base_word) == Counter(comparator) and base_word != comparator


def detect_anagrams(word, options):
    return [option for option in options if is_anagram(word.lower(), option.lower())]