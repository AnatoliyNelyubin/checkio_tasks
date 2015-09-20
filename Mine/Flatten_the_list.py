def flat_list(a):
    fa = []
    for i in a:
        if type(i) == list: fa += (flat_list(i))
        else: fa += [i]
    return fa