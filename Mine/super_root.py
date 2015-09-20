def super_root(number):
    epsilon = 0.001
    lower_border = 1
    upper_border = 10
    root = (upper_border - lower_border) / 2 + lower_border
    guess = root ** root
    while abs(guess - number) > epsilon:
        if guess > number:
            upper_border = root
        else:
            lower_border = root
        root = (upper_border - lower_border) / 2 + lower_border
        guess = root ** root
    return root

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
