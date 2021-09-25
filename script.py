# def concatLanguage(l1, l2, res):
#     for k in l1:
#         for j in l2:
#             res.append(k+j)
#     return res

# def powerOfLanguage(l, p):
#     """
#     Step one: Concatenate once
#     """
#     res = concatLanguage(l, l, [])
#     return res


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


# res = powerOfLanguage(["A", "B"], 4)

# print(res)

# print(power(["A", "B"], 4))

# res = powerOfLanguage(["A", "B"], 4) == power(["A", "B"], 4)
# print(res)


alphabet = ['0', '1']
L = ['010', '01', '100']

res_short = []
for i in range(3):
    res_short = res_short + powerOfLanguage(L, i+1)
res_short.sort()
res_short.sort(key = len, reverse = False)
print(res_short[:20])
