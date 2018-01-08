#Bozena and Isabel
#2/22/16
#PSet 4
#wordprops.py

"""Check for various properties of words like whether 
a given word is a palindrome, can be written using only the 
top row of the keyboard, and the number of Scrabble points the
word is worth. Also, remove the i recurrence of a given 
character.
"""


def reverse(s):
    return s[::-1]

def isPalindrome(word):
    """determines whether a word is a palindrome
    (spelled the same backward as forward)"""
    word1 = word.lower()
    return reverse(word1) == word1
    
def isTopRow(word):
    """determines if word can be spelt using only
    the top row of the keyboard: q, w, e, r, t, y, u, i, o, p"""
    word1 = word.lower()
    for i in word1:
        #while i <= len(word1):
        if i not in 'qwertyuiop':            
            return False
    return True
    

def scrabbleScore(word):
    """returns total number of Scrabble points that word is worth
    if (i == "a" or i == "e" or i == "u" or i == "i" or i == "o" or i == "l" or i == "n" or i == "r" or i == "s" or i == "t"):
        return i == 1
    if (i == "d" or i == "g"):
        return i == 2
    if (i == "b" or i == "c" or i == "m" or i == "p"):
        return i == 3
    if (i == "f" or i == "h" or i == "v" or i == "w" or i == "y"):
        return i == 4
    if (i == "k"):
        return i == 5
    if (i == "j" or i == "x"):
        return i == 8
    if (i == "z" or i == "q"):
        return i == 10
    score = 0
    while i <= len(word):
        score += i
    return score"""
    
    score = 0
    word1 = word.lower()
    for i in word1:
        if i in 'aeioulnrst':
            score += 1
        elif i in 'dg':
            score += 2
        elif i in "bcmp":
            score += 3
        elif i in "fhvwy":
            score += 4
        elif i in "k":
            score += 5
        elif i in "jx":
            score += 8
        elif i in "zq":
            score += 10
    return score

def removeChar(s,char):
    """remove the first appearance of char from s. If char is not found returns 
    s unchanged"""
    message=""
    found=False
    s1 = s.lower()
    for c in s1:
        if char==c and not found:
            found=True
        elif char != c or found:
            message += c 
    return message