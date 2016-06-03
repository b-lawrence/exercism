import re
from collections import defaultdict


def word_count(sequence):
    freq = defaultdict(int)
    lowercase_sequence_list = re.split(r'[\W_]+', sequence.lower())
    for word in lowercase_sequence_list:
        if word:
            freq[word] += 1
    return freq
