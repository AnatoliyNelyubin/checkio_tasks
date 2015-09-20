def convert(numerator, denominator):
    EPSILON = 0.00000001
    # The length of the repetition is always less or equal than denominator -1
    MAXIMUM_NUMBER_OF_DIGITS = denominator  * 5
    integer, fraction = int(numerator // denominator), numerator % denominator
    integer_part = str(integer) + '.'
    fraction_part = ''
    number_of_digits = 0
    # Here we will get as many figures in a fraction part as we want (without rounding!)
    while fraction > EPSILON and number_of_digits < MAXIMUM_NUMBER_OF_DIGITS:
        fraction *= 10
        while fraction < denominator:
            fraction *= 10
            fraction_part += '0'
        integer, fraction = int(fraction // denominator), fraction % denominator
        fraction_part += str(integer)
        number_of_digits += 1
    # print("fraction_part = {}, len of it is {}".format(fraction_part, len(fraction_part)))
    if len(fraction_part) >= MAXIMUM_NUMBER_OF_DIGITS:
        # If we have repeating decimals we should analyse them using tortoise and hare algorithm
        tortoise_index, hare_index = 1, 2
        # Actually here I am trying to compare the slice of my string because comparing just one
        # number does not help.
        while fraction_part[tortoise_index: tortoise_index + denominator] !=\
                fraction_part[hare_index: hare_index + denominator]:
            tortoise_index += 1
            hare_index += 2
            # now we will find the start of the period which is "tortoise_index"
        tortoise_index = 0
        while fraction_part[tortoise_index: tortoise_index + denominator] !=\
                fraction_part[hare_index: hare_index + denominator]:
            tortoise_index += 1
            hare_index += 1
        loop_start = tortoise_index
        # now we will find the length of period
        hare_index += 1
        length_of_period = 1
        while fraction_part[tortoise_index: tortoise_index + denominator] !=\
                fraction_part[hare_index: hare_index + denominator]:
            hare_index += 1
            length_of_period += 1
        # print("sequence = {}, begining of loop = {}, numerator = {}, denomerator = {}, length of period = {}"
        #       .format(fraction_part, tortoise_index, numerator, denominator, length_of_period))
        fraction_part = fraction_part[:loop_start] + '(' + fraction_part[loop_start:loop_start + length_of_period] + ')'
    return integer_part + fraction_part

print(convert(58, 23))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
