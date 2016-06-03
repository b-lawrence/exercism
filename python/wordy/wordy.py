import re
import operator

ops_map = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied by': operator.mul,
    'divided by': operator.floordiv,
}
ops_choices = '|'.join(ops_map.keys())


def extract_data(regex, word_problem):
    print(regex)
    result = re.search(regex, word_problem, flags=re.I)
    print(result)
    return result.groups() if result else None


def calculate_a_op_b(a, op, b):
    if op in ops_map:
        return ops_map[op](int(a), int(b))


def calculate_a_op_b_op_c(a, op1, b, op2, c):
    if op1 in ops_map and op2 in ops_map:
        partial_result = ops_map[op1](int(a), int(b))
        return ops_map[op2](partial_result, int(c))


def calculate(word_problem):
    for regex, fn in regex_map:
        data = extract_data(regex, word_problem)
        if data is not None:
            return fn(*data)
    raise ValueError()


regex_map = [
    (r'(-?\d+) ({0}) (-?\d+) ({0}) (-?\d+)'.format(ops_choices), calculate_a_op_b_op_c),
    (r'(-?\d+) ({0}) (-?\d+)'.format(ops_choices), calculate_a_op_b)
]