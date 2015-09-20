def checkio(expression):
    mystack = []
    pairs = {']': '[', '}': '{', ')': '('}
    for i in expression:
        if i in pairs.values():
            mystack.append(i)
        if i in pairs.keys():
            try:
                last = mystack[-1]
            except IndexError:
                return False
            else:
                if last != pairs[i]:
                    return False
                mystack.pop()

    return len(mystack) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"