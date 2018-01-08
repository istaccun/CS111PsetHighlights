# Add your comments here
#

__author__='Isabel Staccuneddu'

from turtle import *

#  ----------write your code here -----------
def shrub(trunkLength, angle, shrinkFactor, minLength):
    """Draws a shrub with the specified parameters.
    Returns a tuple consisting of the total number of branches
    and the total length of the branches (including the trunk)
    of the shrub"""
    if trunkLength <= minLength:
        # base case
        # No branches are made, no trunk is drawn = no distance travelled, returns 0
        return 0,0

    else:

        # Totals begin with basic tree (just the trunk)
        totalBranches = 1 
        totalLength  = trunkLength

        #Action: Tree
        fd(trunkLength)
        rt(angle)
        shrub(trunkLength*shrinkFactor, angle, shrinkFactor, minLength)
        lt(angle)
        bk(trunkLength)
        fd(trunkLength)
        rt(angle)
        shrub(trunkLength*shrinkFactor*shrinkFactor, angle, shrinkFactor, minLength)
        lt(angle)
        bk(trunkLength)
        
        #fd(trunkLength)
        #lt(angle)
        #fd(trunkLength)
        #rt(angle)
        #fd(trunkLength)
        #lt(angle)
        #fd(trunkLength)

        # Recurse
        branchesDrawn, lengthTravelled = shrub(trunkLength*shrinkFactor, angle, shrinkFactor, minLength)

        # Update counters post recursion
        totalBranches += branchesDrawn 
        totalLength  += lengthTravelled 

        # Return the counters
        return totalBranches,totalLength

# --------------------------------------------

def testShrub (trunkLength, angle, shrinkFactor, minLength):
    """Testing code for shrub function."""    
    setup(600, 600, 0, 0) # Set size of turtle window and bring it to the top of the screen
    speed(3) # Set the speed; 0=fastest, 1=slowest, 6=normal  
    pensize(1) # Choose a pen thickness
    
    # Move turtle to lower middle pointing up 
    setpos(0, -(window_height()/2.0 - 20))
    setheading(90)

    clear() # Clear any existing turtle drawings
    testInputString = ('shrub(' + str(trunkLength) + ', ' 
                       + str(angle) + ', ' + str(shrinkFactor) 
                       + ', ' + str(minLength) + ')')

    # Put testInputString in title at top of window
    title(testInputString)
      
    # Draw shrub and get returned result  
    numBranches, lengthBranches = shrub(trunkLength, angle, shrinkFactor, minLength)
    
    testOutputString = testInputString + ' -> ' + str(numBranches) + ' branches, '+ str(lengthBranches) + ' total branch length'
            
    # Put testOutputString in title at top of window 
    title(testOutputString)
    
    # Make sure the window can close on click
    exitonclick()
    
# Uncomment each of the lines below to test. 
# You can only run one invocation of testShrub at a time.
#testShrub(80,20,0.5,10)
testShrub(100, 15, 0.8, 60)
#testShrub(100, 15, 0.8, 50)
#testShrub(100, 15, 0.8, 10)
#testShrub(100, 30, 0.82, 10)
#testShrub(200, 90, 0.75, 10)

