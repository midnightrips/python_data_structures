def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = list(phrase)

    phrase_list.reverse()

    reversed_str = ''.join(phrase_list)

    print(f"'{reversed_str}'")
