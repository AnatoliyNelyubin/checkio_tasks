def checkio(number):
    best_radix = 0
    for radix in range(2, 37):
        try:
            result = int(number, base=radix)
        except ValueError:
            pass
        else:
            if result % (radix - 1) == 0:
                best_radix = radix
                break
    return best_radix

# print(checkio("1010101011"))
# exit()
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
