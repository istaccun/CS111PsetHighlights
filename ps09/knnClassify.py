# PS 9: Gender Classifier of Names
# April 14th, 2016 
# Tanya and Isabel 

"""
Credits: This task was written by Prof. Sravana Reddy for CS111 in Fall 2015.
She will teach an entire course in Machine Learning in Spring 2017.
If you enjoy this problem, consider taking that course in 2017.
"""


from math import sqrt
import string
import sys
import os

###############################################################################
# Feature Functions for Step 1: two are given, you need to write four more.

def length(name):
    """Feature function for the length of name. Return a list with 
       one tuple.
    """
    return [('length', len(name))]

  
def vowels(name):
    """Feature function for the number of vowels in name. Returns
       a list with one tuple.
    """
    def isVowel(c):
        return c in 'aeiouy'
    return [('vowels', len(filter(isVowel, name)))]

  
# Write the four additional feature functions below

def hardCons(name): 
    def isCon(c):
        return c in 'ptkbdg'
    return [('hard', len(filter(isCon, name)))]
    
def countLetters(name): 
    lowerString = string.lowercase  
    def count(letter): 
        letterCount = name.count(letter) 
        return ('count -' + letter, letterCount)
    return map(count, lowerString) 
    
def lastLetter(name): 
    lowerString = string.lowercase  
    def count(letter): 
        if name[-1] == letter: 
            return ('last -' + letter, int(True))
        else: 
            return ('last -' + letter, int(False))
    return map(count, lowerString) 
    
def firstLetter(name): 
    lowerString = string.lowercase  
    def count(letter): 
        if name[0] == letter: 
            return ('last -' + letter, int(True))
        else: 
            return ('last -' + letter, int(False))
    return map(count, lowerString) 

###############################################################################
# Feature Combination for Step 2

def combine(featureFunc1, featureFunc2):
    """Returns a function that, when applied to a name, 
       returns a feature vector combining the feature vectors 
       from featureFunc1 and featureFunc2.
    """
    def concatenateCombine(word):
        return featureFunc1(word) + featureFunc2(word)
    return concatenateCombine
    

def combineMany(listOfFeatureFuncs):
    """Returns a function that, when applied to a name, returns a feature 
       vector combining the feature vectors from featureFunc1 and featureFunc2.
    """
    return reduce(combine, listOfFeatureFuncs) 
    
###############################################################################
# Classification for Step 3

# Helper Function: don't change.
def euclideanDistanceFrom(v):
    """Returns a function that takes a vector and computes the distance between 
       that vector and v.
    """
    def euclideanDistanceHelper(w):
        """distance between vectors v and w"""
        def squareDiff(i):
            """square of difference between elements in ith position of 
               vectors v and w
            """
            return (v[i][1] - w[i][1])**2
        return sqrt(sum(map(squareDiff, range(len(v)))))
    return euclideanDistanceHelper


# Step 3a
def buildTrainingVectors(featurefunc, trainfile):
    """Read names from trainfile, return a list of tuples,
       where each tuple in the list corresponds to a name.
       Each tuple is of the form (genderlabel, featurevector),
       where genderlabel is the gender of the name,
       and featurevector is the feature vector of the name under featurefunc.
    """
    with open(trainfile, 'r') as fileObj:
        trainFileLines = fileObj.readlines()  
            
    def createTuples(line): 
        splitLine = line.split() 
        return (splitLine[1], featurefunc(splitLine[0])) 

   
    return map(createTuples, trainFileLines)

# Step 3b
def labelsSortedByDistance(testvector, trainingVectors):
    """Create a list of (genderlabel, distance) tuples from trainingVectors
       (trainingVectors is a list of (gender, featvec) tuples, 
       of the type returned by buildTrainingVectors).
       The distance is the Euclidean distance between featvec and testvector.
       Sort this list of tuples by distance
    """
    func = euclideanDistanceFrom(testvector)
    
    def createVector(trainingVector): 
        return (trainingVector[0], func(trainingVector[1])) 
    
    def getItem2(tup): 
        return tup[1]  
        
    return sorted(map(createVector, trainingVectors), key=getItem2) 
         
# Step 3c
def predictGender(featurefunc, testname, trainingVectors, k):
    """Find the k nearest training vectors to testname's
       feature vectors. Return the most common label among those 
       nearest training vectors.
    """
    featureVector = featurefunc(testname)   
    listOfTuples = labelsSortedByDistance(featureVector, trainingVectors) 
    
    listOfGender = map(lambda x: x[0], listOfTuples[:k]) 
    number = map(lambda x: (listOfGender.count(x), x), listOfGender) 
    return max(sorted(number, reverse=True))[1]   
 
   
def computeAccuracy(featurefunc, testfile, trainingVectors, k):
    """Go through each name in testfile, predict its gender label,
       and print the predictions for each example as instructed.
       Return the accuracy (the proportion of examples for which 
       the labels are correctly predicted).
    """
    with open(testfile, 'r') as fileObj:
        testFileLines = fileObj.readlines()
        nameGenderList = map(lambda x: x.split(),testFileLines)  
        
    correctCount = 0     
    
    for name in nameGenderList:
        if name[1] == predictGender(featurefunc, name[0], trainingVectors, k): 
            print name[0] + "  " + name[1] + " " + predictGender(featurefunc, name[0], trainingVectors, k) + " " + "CORRECT"
            correctCount += 1      
        else: 
            print name[0] + "  " + name[1] + " " + predictGender(featurefunc, name[0], trainingVectors, k) + " " + "WRONG" 
            
    totalCorrectCount = int(correctCount)/float((len(nameGenderList))) 
    return totalCorrectCount 

###############################################################################
# Step 4: Run the entire program

def main():
    """Runs the classification program with command line arguments"""
    try: 
        k = int(sys.argv[1])
        featurefunc = sys.argv[2:]
        listOfFunctions = map(eval, featurefunc) 
        
        funcVals = combineMany(listOfFunctions) 
        trainingVectors = buildTrainingVectors(funcVals, 'train.txt')
        
        result = computeAccuracy(funcVals, "test.txt", trainingVectors, k)
         
        print "Accuracy: " + str(result) 
 
    except:
        print "USAGE: Arguments to this program: k featurefunc1 featurefunc2 ... \nk is a positive integer number. \nEach featurefuncn is a valid feature function."  
        

if __name__=='__main__':  # invoke main() when program is run
    main()