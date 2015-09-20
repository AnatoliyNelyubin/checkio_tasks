def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    if len(args) == 1:
        return args[0]
    else:
        list_of_gcds = []
        for item in range(len(args) - 1):
            first, second = args[item], args[item+1]
            the_rest = None
            while the_rest != 0:
                the_rest = first % second
                first = second
                second = the_rest
            list_of_gcds.append(first)
        return greatest_common_divisor(*list_of_gcds)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(4) == 4, "Very Simple"
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"