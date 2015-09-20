def find_word(message):
    import string
    message_list = ''.join(filter(lambda x: x not in string.punctuation, message)).lower().split()
    matrix = [[0 for col in range(len(message_list))] for row in range(len(message_list))]
    for row in range(len(message_list)):
        for col in range(len(message_list)):
            if col == row:
                continue
            if message_list[row][0] == message_list[col][0]:
                matrix[row][col] += 10
            if message_list[row][-1] == message_list[col][-1]:
                matrix[row][col] += 10
            if len(message_list[row]) >= len(message_list[col]):
                matrix[row][col] += len(message_list[col])/len(message_list[row]) * 30
            else:
                matrix[row][col] += len(message_list[row])/len(message_list[col]) * 30
            matrix[row][col] +=  len(set(message_list[row]).intersection(set(message_list[col]))) / \
                                 len(set(message_list[row] + message_list[col])) * 50
    keyword, gr_average = '', None
    for row in range(len(message_list)):
        if gr_average is None or sum(matrix[row])/len(matrix[row]) >= gr_average:
            gr_average = sum(matrix[row])/len(matrix[row])
            keyword = message_list[row]
    return keyword

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"