VOWELS = "aeiouy"
CNSNNTS = "bcdfghjklmnpqrstvwxz"

def translate(phrase):
    index, new_phrase = 0, ''
    while index < len(phrase):
        new_phrase += phrase[index]
        if phrase[index] in CNSNNTS:
            index += 2
        elif phrase[index] in VOWELS:
            index += 3
        else:
            index += 1

    return new_phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
