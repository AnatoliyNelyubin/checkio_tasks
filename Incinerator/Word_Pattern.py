def check_command(pattern, command):
    # print(bin(pattern)[2:].rjust(len(command),'0'), command)
    number_of_overlaps = 0
    for x, y in zip(bin(pattern)[2:].rjust(len(command), '0'), command):
        if x == '0' and y.isdigit() or x == '1' and not y.isdigit():
            number_of_overlaps += 1
    return number_of_overlaps == len(command) >= len(bin(pattern)[2:])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, "12a0b3e4") == True, "42 is the answer"
    assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, "478103487120470129") == True, "Any number"
    assert check_command(127, "Checkio") == True, "Uppercase"
    assert check_command(7, "Hello") == False, "Only full match"
    assert check_command(8, "a") == False, "Too short command"
    assert check_command(5, "H2O") == True, "Water"
    assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"