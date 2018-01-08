# Isabel Staccuneddu
# PSet 7
# hourglass.py
# March 15th, 2016

def hourglass(indent, width, char1, char2):
    if width == 1 or width == 2:
        print (" "*indent) + char1*width + (" "*indent)
    else:
        print (" " * indent) + (char1 * width) + (" " * indent)
        hourglass(indent+1, width-2, char2, char1)
        print (" " * indent) + (char1 * width) + (" " * indent)
        
hourglass(5, 7, "*", "-")