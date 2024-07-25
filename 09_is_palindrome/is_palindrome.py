def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    no_space_phrase = phrase.replace(" ", "")

    lwr_phrase = no_space_phrase.lower()

    phrase_list = list(lwr_phrase)

    phrase_list.reverse()

    reversed_str = ''.join(phrase_list)

    if reversed_str != lwr_phrase:
        return False
    else:
        return True