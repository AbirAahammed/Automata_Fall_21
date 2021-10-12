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
dfa = DFA(
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

l = ['0','1']

def test(i):
    ls = powerOfLanguage(l, i)
    for k in ls:
        try:
            dfa.read_input(k)
            if ('110' in k):
                print('Test failed Accepted ', k)
        except RejectionException:
            if (not '110' in k):
                print('Test failed Reject')

if __name__ == '__main__':
    i = 1
    with Pool(5) as p:
        p.map(test, [i+1 for i in range(20)])

