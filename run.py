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


def perform_action(val):
    if val['a'] == '' and val['action'] == '-':
        val['action'] = ''
        val['b'] = -14
        return val['b']
    val['a'] = float(val['a'])
    val['b'] = float(val['b'])
    a = val['a']
    b = val['b']
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '^': a ** b,
        '%': a % b,
        '!': a,  # TODO
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
    for action in actions:
        if contains(val, action) and current == -1:
            current = action
        elif contains(val, action) and actions[action] > actions[current]:
            current = action
    return current


def get_first_numbers(val):
    count_start = 0
    for char in val:
        if char in actions:
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
        to_return['b'] = val
        to_return['action'] = ''
        to_return['a'] = ''
        return to_return

    if val[0] in actions and strongest_action(val) == val[0]:
        to_return['b'] = val[:len(val)]
        to_return['action'] = ''
        to_return['a'] = ''
        return to_return
    for char in val:
        count_start += 1
        count_symbol += 1
        if char == strongest_action(val):
            to_return['a'] = val[count_start - count_symbol:count_start - 1]
            to_return['b'] = get_first_numbers(val[count_start:])
            to_return['action'] = val[count_start - 1:count_start]
            return to_return
        elif char in actions:
            count_symbol = 0


def replace_action(val, action):
    val = val.replace(action['a'] + action['action'] + action['b'], str(perform_action(action)))
    return val


def calculate_block(val):
    next = get_next_action(val)
    while next['action'] != '':
        print 'next action is %s ' % next
        val = replace_action(val, next)
        print 'current val is %s ' % val
        next = get_next_action(val)
        print '-------------'
    return next['b']

def main():
    val = raw_input("Enter ")
    # val = '5+4-18'
    val = delete_spaces(val)
    result = calculate_block(val)
    print 'result is %s ' % result
    main()


main()
