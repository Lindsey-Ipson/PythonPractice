def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(' ')
    newPhrase = []
    for word in words:
        newPhrase.append(word.capitalize())
    return ' '.join(newPhrase)