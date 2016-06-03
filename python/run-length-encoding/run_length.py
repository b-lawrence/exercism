import re
from itertools import groupby


def get_group_length(group):
    length = len(list(group))
    return str(length) if length > 1 else ''


def encode(decoded_data):
    return ''.join(get_group_length(letter_group) + key for key, letter_group in groupby(decoded_data))


def decode(encoded_data):
    num_letter_pairs = re.findall(r'(\d*)(\D)', encoded_data, flags=re.I)
    return ''.join(letter * int(number or 1) for number, letter in num_letter_pairs)
