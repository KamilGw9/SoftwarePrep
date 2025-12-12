"""

Given a string containing letters, digits, and symbols, determine if it reads the same 
forwards and backwards when considering only alphabetic characters (case-insensitive).

"""


# 11/15  passed

def isAlphabeticPalindrome(code):
    
    getstr = ''.join(s.lower() for s in code if s.isalpha())
    return 1 if getstr == getstr[::1] else 0


# 15/15

def isAlphabeticPalindrome(code):
    i, j = 0, len(code) - 1

    while i < j:
        
        while i < j and not code[i].isalpha():
            i += 1
        
        while i < j and not code[j].isalpha():
            j -= 1

        if code[i].lower() != code[j].lower():
            return 0

        i += 1
        j -= 1

    return 1