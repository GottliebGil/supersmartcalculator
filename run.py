import math
actions = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 3,
    '!': 4,
    '@': 5,
    '$': 5,
    '&': 5
}
one_parameter_actions = ['!']

def perform_action(val):
    """Receives an action type (two parts and an action) and performs an action on it"""
    if val['a'] == '' and val['action'] == '-':
        val['action'] = ''
        val['b'] = -14
        return val['b']
    if val['a'] != '':
        val['a'] = float(val['a'])
    if val['b'] != '':
        val['b'] = float(val['b'])
    a = val['a']
    b = val['b']
    if val['b'] == '':
        return {
            '!': math.factorial(a)  # TODO
        }[val['action']]
    else:
        return {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b,
            '^': a ** b,
            '%': a % b,
            '@': (a + b) / 2,
            '$': max(a, b),
            '&': min(a, b)
        }[val['action']]


def delete_spaces(val):
    """Removes all spaces from the string"""
    if type(val) is str:
        return filter(lambda x: x != ' ', val)
    return val


def contains(val, char):
    """Returns True if string contains char"""
    if type(val) is str:
        return filter(lambda x: x == char, val) != ''
    else:
        return False


def strongest_action(val):
    """Returns the strongest action in a string"""
    current = -1
    index = 0
    for char in val:
        if char in actions and current == -1 and index != 0:
            current = char
        elif char in actions and index != 0 and actions[char] > actions[current]:
            current = char
        index += 1
    return current


def actions_counter(val):
    """Returns the number of actions left to calculate in value"""
    current = 0
    for char in val:
        if char in actions:
            current += 1
    return current


def get_first_numbers(val):
    count_start = 0
    for char in val:
        if char in actions and count_start > 0:
            return val[:count_start]
        if count_start == len(val) - 1:
            return val
        count_start += 1


def get_next_action(val):
    to_return = {
        'b': '',
        'action': '',
        'a': ''
    }
    count_start = 0
    count_symbol = 0

    if strongest_action(val) == -1:
        to_return['b'] = val or ''
        to_return['action'] = ''
        to_return['a'] = ''
        return to_return

    if val[0] in actions and actions_counter(val) == 1 and strongest_action(val) == val[0]:
        to_return['b'] = val[:len(val)]
        to_return['action'] = ''
        to_return['a'] = ''
        return to_return
    for char in val:
        count_start += 1
        count_symbol += 1
        if char == strongest_action(val) and char in one_parameter_actions:
            to_return['a'] = val[count_start - count_symbol:count_start - 1] or ''
            to_return['b'] = ''
            to_return['action'] = val[count_start - 1:count_start]
            return to_return

        if char == strongest_action(val) and count_start != 1:
            to_return['a'] = val[count_start - count_symbol:count_start - 1] or ''
            to_return['b'] = get_first_numbers(val[count_start:]) or ''
            to_return['action'] = val[count_start - 1:count_start] or ''
            return to_return
        elif char in actions and count_start != 1:
            count_symbol = 0


def replace_action(val, action):
    val = val.replace(action['a'] + action['action'] + action['b'], str(perform_action(action)))
    return val


def calculate_block(val):
    # Firstly, I'll calculate all the parentheses
    block = get_block(val)
    while block != '':
        calculated = calculate_block(block)
        val = val.replace('(' + block + ')', calculated)
        block = get_block(val)
    next = get_next_action(val)
    while next['action'] != '':
        print 'next action is %s ' % next
        val = replace_action(val, next)
        print 'current val is %s ' % val
        next = get_next_action(val)
        print '-------------'
    return next['b']


def get_block(val):
    indent = 0
    block = ''
    for char in val:
        if char == ')':
            indent += -1
        if indent == 0 and block != '':
            return block
        if indent > 0:
            block += char
        if char == '(':
            indent += 1
    return ''


def main():
    val = raw_input("Enter ")
    val = delete_spaces(val)
    result = calculate_block(val)
    print 'result is %s ' % result
    main()


main()
