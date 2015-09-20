def convert(numer, denom):
    intquo, rem = divmod(numer, denom)
    decquo = ''
    remlog = [rem]
    while rem > 0:
        quo, rem = divmod(rem * 10, denom)
        decquo += str(quo)
        if rem in remlog:
            start = remlog.index(rem)
            return  '{}.{}({})'.format(intquo, decquo[:start], decquo[start:])
        remlog.append(rem)
    return '{}.{}'.format(intquo, decquo)

print(convert(1, 99))