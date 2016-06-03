import re
import operator

ops = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied': operator.mul,
    'divided': operator.floordiv,
}


def calculate(word_problem):
    stop_words = 'what|which|greater|is|by|,|\?'
    filtered_word_problem = re.sub(r'({0})'.format(stop_words), '', word_problem, flags=re.I)
    tokens = list(filter(lambda token: bool(token) == True, filtered_word_problem.split(' ')))
    tokens.reverse()

    def do_operation():  # requires three tokens to execute each time.
        try:
            get_next_token = tokens.pop
            operand_1 = int(get_next_token())
            _operator = get_next_token()
            operand_2 = int(get_next_token())
            tokens.append(ops[_operator](operand_1, operand_2))
            if len(tokens) >= 3:
                do_operation()
        except Exception:
            raise ValueError('Problem does\'nt compute!')
    do_operation()
    return tokens[0]
