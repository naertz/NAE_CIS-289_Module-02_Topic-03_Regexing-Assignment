"""
Program:               regex_dune_quote.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-08

Uses on a regex on a Dune quote to calculate number of words in certain conditions and returns updated quote with 'you' version.
"""

from re import IGNORECASE, search, split, sub

DUNE_QUOTE = '"I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain." – Frank Herbert, Dune'

if __name__ == '__main__':
    # Split Dune quote to a list of strings.
    split_dune_quote = split(r'\s', DUNE_QUOTE)

    # Get words containing 'f'.
    words_containing_f = []

    for word in split_dune_quote:
        if search('f', word, flags=IGNORECASE) is not None:
            words_containing_f.append(word)

    print(f'Number of words containing the letter f (case insensitive): {str(len(words_containing_f))}')

    # Get words starting with 'f'.
    words_starting_with_f = []

    for word in split_dune_quote:
        if search('^f', word, flags=IGNORECASE) is not None:
            words_starting_with_f.append(word)

    print(f'Number of words starting with the letter f (case insensitive): {str(len(words_starting_with_f))}')

    # Get words matching whole word 'not'.
    words_matching_not = []

    for word in split_dune_quote:
        if search(r'\bnot\b', word) is not None:
            words_matching_not.append(word)

    print(f'Number of times the word \'not\' appears: {str(len(words_matching_not))}')

    # Change Dune quote to 'you'.
    you_dune_quote = sub(r'\"I', '"You', DUNE_QUOTE)
    you_dune_quote = sub(r'\.\sI', '. You', you_dune_quote)
    you_dune_quote = sub(r'I', 'you', you_dune_quote)
    you_dune_quote = sub(r'my', 'your', you_dune_quote)
    you_dune_quote = sub(r'me', 'you', you_dune_quote)

    # Print 'you' Dune quote.
    print(you_dune_quote)
