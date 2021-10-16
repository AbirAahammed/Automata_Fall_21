from automata.fa.dfa import DFA
from automata.base.exceptions import RejectionException
from multiprocessing import Pool
def power(l1, p):
    if p == 1:
        return l1
    else:
        res = power(l1, p - 1)
        return concatLanguage(res, l1)

def concatLanguage(l1, l2):
    res = []
    for k in l1:
        for j in l2:
            res.append(k+j)
    return res

def powerOfLanguage(l, p):
    """
    Step one: Concatenate once
    """
    res = l
    for i in range(p - 1):
        res = concatLanguage(res, l)
    return res

# DFA which matches all binary strings ending in an odd number of '1's
dfa_a = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'C', '1': 'B'},
        'B': {'0': 'E', '1': 'B'},
        'C': {'0': 'C', '1': 'D'},
        'D': {'0': 'C', '1': 'D'},
        'E': {'0': 'E', '1': 'B'},
    },
    initial_state='A',
    final_states={'D', 'E'}
)


dfa_b = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'C', '1': 'B'},
        'B': {'0': 'E', '1': 'D'},
        'C': {'0': 'A', '1': 'D'},
        'D': {'0': 'E', '1': 'B'},
        'E': {'0': 'E', '1': 'E'},
    },
    initial_state='A',
    final_states={'B', 'C'}
)

dfa_c = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'A', '1': 'C'},
        'C': {'0': 'D', '1': 'C'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'A', 'B', 'C'}
)

def validate_a(s):
    return s[0] != s[-1]

def validate_b(s):
    try:
        i=s.index('1')
        zero, one =  s[:i], s[i:]
        if '1' in zero:
            return False
        if '0' in one:
            return False
        return len(s) % 2 == 1
    except ValueError:
        return len(s) % 2 == 1
    
def validate_c(s):
    return '110' not in s
l = ['0','1']

def test_a(i):
    ls = powerOfLanguage(l, i)
    for k in ls:
        try:
            dfa_a.read_input(k)
            if (not validate_a(k)):
                print('Test A failed Accepted ', k)
            print("{}|A|accepted".format(k))
        except RejectionException:
            print("{}|A|rejected".format(k))
            if (validate_a(k)):
                print('Test A failed Reject ', k)

def test_b(i):
    ls = powerOfLanguage(l, i)
    for k in ls:
        try:
            dfa_b.read_input(k)
            if (not validate_b(k)):
                print('Test B failed Accepted ', k)
            print("{}|B| accepted".format(k))
        except RejectionException:
            print("{}|B|rejected".format(k))
            if (validate_b(k)):
                print('Test B failed Reject ', k)
def test_c(i):
    ls = powerOfLanguage(l, i)
    for k in ls:
        try:
            dfa_c.read_input(k)
            if (not validate_c(k)):
                print('Test C failed Accepted ', k)
            print("{}|C| accepted".format(k))
        except RejectionException:
            print("{}|C|rejected".format(k))
            if (validate_c(k)):
                print('Test C failed Reject ', k)

if __name__ == '__main__':
    print('String | A/R\n-|-')
    test_i = 10
    res_a = []
    res_b = []
    res_c = []
    with Pool(5) as p:
        p.map(test_a, [i+1 for i in range(test_i)])
    with Pool(5) as p:
        p.map(test_b, [i+1 for i in range(test_i)])
    with Pool(5) as p:
        p.map(test_c, [i+1 for i in range(test_i)])