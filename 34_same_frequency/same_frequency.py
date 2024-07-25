def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    counts1 = {}
    counts2 = {}

    for char in str1:
        counts1[char] = str1.count(char)
    
    for char in str2:
        counts2[char] = str2.count(char)

    if counts1 == counts2:
        return True
    else:
        return False