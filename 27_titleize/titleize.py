def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    import string

    return string.capwords(phrase) # https://www.geeksforgeeks.org/python-string-capwords-method/

    # solution uses return phrase.title()