def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'

    lwr_phrase = phrase.lower()

    counts = {}

    for letter in lwr_phrase:
        if letter in vowels:
            counts[letter] = lwr_phrase.count(letter)

    return counts