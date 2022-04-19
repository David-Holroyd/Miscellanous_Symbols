import random
#  List of miscellaneous unicode symbols: https://en.wikipedia.org/wiki/Miscellaneous_Symbols

ALPHABET = {'A': ['⛰', '⛺'], 'B': ['♭'], 'C': ['☪', '☾', '⚸'], 'D': ['♢', '⛛', '♺'],
            'E': ['⚟'], 'F': ['⛿'], 'G': ['♋', '⚲'], 'H': ['♄', '♓'], 'I': ['♙', '⚘'],
            'J': ['☂'], 'K': ['⛕'], 'L': ['☇'], 'M': ['♏'], 'N': ['♑', '⚻'],
            'O': ['☉', '☮', '☯', '⚙', '⚽', '⚾', '⛔', '⛣', '⛭', '⛮', '⛯'], 'P': ['☧', '♇', '⚐'],
            'Q': ['⚼'], 'R': ['☈'], 'S': ['⚕'], 'T': ['☦', '☨', '☩', '♰', '♱', '⚚'], 'U': ['☋', '⛎'], 'V': ['⚺'],
            'W': ['♆'], 'X': ['☒', '☓', '☠', '⚒', '⚔', '⚹', '⛌', '⛒', '⛝'], 'Y': ['♉'], 'Z': ['☡']}

stop = False
while not stop:
    word = input("Please enter a word to translate: ").upper()

    if word == 'STOP':
        stop = True
    else:
        word_converted = ''
        word_unique_letters = {}

        for letter in word:
            if letter in [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', ',', '.', "'", '"', ';', ':',
                          '-', '_', '/', '{', '}', '\\', '|', '~', '`', '<', '>', '+', '='
                          ]:
                chosen_symbol = letter
            elif letter in word_unique_letters:
                chosen_symbol = word_unique_letters[letter]
            else:
                symbol_list = ALPHABET[letter]
                num_symbols = len(symbol_list)
                chosen_symbol = symbol_list[random.randint(0, num_symbols-1)]
                word_unique_letters[letter] = chosen_symbol
            word_converted = word_converted + chosen_symbol

        print(word_converted)





