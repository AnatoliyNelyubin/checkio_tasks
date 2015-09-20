def digit_stack(commands):
    a, counter = [], 0
    for i in commands:
        if i.split()[0] == "PUSH":
            a.append(int(i.split()[1]))
        elif i == "POP":
                counter += a.pop() if a else 0
        elif i == "PEEK":
                counter += a[-1] if a else 0
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"