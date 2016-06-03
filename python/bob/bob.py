def hey(ulterance):

    ulterance = ulterance.strip()

    if not ulterance:
        response = 'Fine. Be that way!'
    elif ulterance.isupper():
        response = 'Whoa, chill out!'
    elif ulterance.endswith('?'):
        response = 'Sure.'
    else:
        response = 'Whatever.'

    return response
