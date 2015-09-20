VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import string

def checkio(text):
    words_counter = 0
    for i in string.punctuation:
        text = text.replace(i, ' ')
    text = text.upper()
    wordlist = text.split()
    for word in wordlist:
        if len(word) > 1:
            if word[0] in VOWELS:
                word_vowels = set(word[::2])
                word_consonants = set(word[1::2])
            else:
                word_vowels = set(word[1::2])
                word_consonants = set(word[::2])
            word_vowels.difference_update(set(VOWELS))
            word_consonants.difference_update(set(CONSONANTS))
            if not word_vowels and not word_consonants:
                words_counter += 1
    return words_counter


#  These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"