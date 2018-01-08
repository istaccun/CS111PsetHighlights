# Isabel S
# 2/28/16
# Task 2 - Pset 5

"""Search for words with certain special properties in a
list of English words
"""

from vocabulary import englishwords
from wordprops import isPalindrome, isTopRow, scrabbleScore

def listPalindromes():
    """return a list of all palindromes in englishwords that
    are more than one letter long."""
    list1 = []
    for word in englishwords:
        if len(word) > 1 and isPalindrome(word) == True:
            list1.append(word)
    print list1
    
def listTopRowWords(minLength):
    """returns a list of all english words that can be written 
    with only the top row of the keyboard, and are at least minLength
    letters long."""
    list2 = []
    for word in englishwords:
        if len(word) >= minLength and isTopRow(word) == True:
            list2.append(word)
    print list2
    
def listGoodScrabbleWords(minScore):
    """return a list of all english words 
    that have score at least minScore and are no more 
    than 15 letters long.
    """
    list3 = []
    for word in englishwords:
        if scrabbleScore(word) >= minScore and len(word) <= 15:
            list3.append(word)
    print list3

listPalindromes()
listTopRowWords(8)
listGoodScrabbleWords(35)