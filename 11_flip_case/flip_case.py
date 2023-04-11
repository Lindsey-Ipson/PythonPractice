def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase = []
    for letter in phrase:
        if letter.lower() == to_swap or letter.upper() == to_swap:
            if letter.islower():
                newPhrase.append(letter.upper())
            elif letter.isupper():
                newPhrase.append(letter.lower())
        else: newPhrase.append(letter)

    return ('').join(newPhrase)