def checkio(data):

    return eval(str(data)[1:-1].replace(',','+'))

print(checkio([1,2,3]))
print(checkio([43,-10,68,84,91,71,-10,-80,38]))  # result - 295