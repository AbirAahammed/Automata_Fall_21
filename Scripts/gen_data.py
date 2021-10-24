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
    if p == 0:
        return []
    res = l
    for i in range(p - 1):
        res = concatLanguage(res, l)
    return res


from multiprocessing import Pool
import sys

def powerOfLanguageMod(p):
    return powerOfLanguage(['0', '1'], p)

if __name__ == '__main__':
    res = []
    # if ()
    with Pool(5) as p:
        res = p.map(powerOfLanguageMod, [i for i in range(int(sys.argv[1])+ 1)])
    res = [j for sub in res for j in sub]
    try:
        with open(sys.argv[2], 'w') as f:
            f.write("\n".join(res))
            f.close()
    except IndexError:
        with open('gendata.txt', 'w') as f:
            f.write("\n".join(res))
            f.close()
        