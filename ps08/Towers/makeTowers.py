# CS111 PS08 Spring 2016
# makeTowers.py
#
# Isabel Staccuneddu
#
#
             
# ---------------- Start of provided code --------------------  
             
# This is the version of the tower function from Lecture. You need to modify it so it
# returns a (multi-line) string rather than printing a (multi-line) string.

def tower(word):
    if len(word)==0:
        return ""
    else:
        return str(word) + "\n" + tower(word[1:])
        
#Testing        
#print tower("word")

# ---------------  end provided code here ----------------------

# Write your definition of your functions here:

def towerify(fileName): #calls the 2 helper functionz
    readFile(fileName)
    writeFile(fileName)
    
# Helper functions

def readFile(fileName): #returns a list of words from the input file
    with open(fileName, 'r') as myFile:
        words = [line.strip() for line in myFile]
    return words
    
def writeFile(fileName): #returns a file with one word on each line from readFile(input file) and renames output file
    fileList = fileName.split('.')
    with open(str(fileList[0])+"Tower"+".txt",'w') as myFile:
        words = readFile(fileName)
        for word in words:
            myFile.write(tower(word) + "\n")
    return myFile