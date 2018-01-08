#Isabel Staccuneddu & Bozena Scheidel
#CS111 PS08
#MArch 30 2016
#makequilts.py


from picture import *

#  ----------write your code here -----------

 #Task 2a 
def quadRecurse(pic1, pic2, levels):
    """Returns an upper right quadrant of a quilt as shown in the assignment."""
    if levels==0:
        return empty()

    else:
        return fourPics((recurseTop(pic1, pic2, levels)),recurseDiag(pic1, pic2, levels),pic1,(recurseRight(pic2, pic1, levels)))
        #return fourPics(fourPics(empty(), empty(), quadRecurse(pic2, pic1, levels-1), quadRecurse(pic2, pic1, levels-1)),fourPics(empty(), empty(),quadRecurse(pic2, pic1, levels-1), quadRecurse(pic2, pic1, levels-1)),pic1,fourPics(empty(), empty(), quadRecurse(pic2, pic1, levels-1), quadRecurse(pic2, pic1, levels-1)))
        #return fourPics((quadRecurse(pic2, pic1, levels-1)),(quadRecurse(pic2, pic1, levels-1)),pic1,pic1)
        
#helper function to recurse to the top
def recurseTop(pic1, pic2, level):
    if level==0:
        return empty()
    #if level==1:
    #    return fourPics(empty(), empty(), pic1, empty())
    #doesnt work cause in recusrion level 1 cant b isolated liek this
        
    else:
        top = recurseTop(pic2, pic1, level-1)
        
        return fourPics(top, top, pic2, pic2)
def recurseRight(pic1, pic2, level):
    if level==0:
        return empty()
    #if level==1:
    #    return fourPics(empty(), empty(), pic1, empty())
    #doesnt work cause in recusrion level 1 cant b isolated liek this
        
    else:
        right = recurseRight(pic2, pic1, level-1)
        return fourPics(pic1, right, pic1, right)

def recurseDiag(pic1, pic2, level):
    if level == 0:
            return empty()
    else:
        diag = recurseDiag(pic2, pic1, level-1)
        return fourPics(recurseTop(pic2, pic1, level-1), diag, pic2, recurseRight(pic1, pic2, level-1))
    
# Task 2b
def quilt(pic1, pic2, levels):
    """Returns the quilt pattern in the assignment."""
    # fill in
    
    return rotations(quadRecurse(pic1, URNest(pic1, pic2), levels))
    

# Define any helper functions below
def UR(p):
    """Returns the picture p nested in the upper right corner"""
    return fourPics(empty(), p, empty(), empty())

def URNest(pic1, pic2):
    """Returns the picture p2 nested in upper right corner of picture p1"""
    return overlay(UR(pic2), quadRecurse(pic1, pic2, levels))


# --------------------------------------------

emptyPic = empty()
redLeaves = leaves('red')
greenLeaves = leaves('forestgreen')
pyTri = triangles('purple', 'yellow') # purple-yellow-triangles
gwTri = triangles('forestgreen', 'lightgrey') # green-whiteish(really-greyish)-triangles

# Uncomment the code below to test your program

# #Testing quadRecurse
#for levels in range(7):
#    q = quadRecurse(pyTri, gwTri, levels)
#    displayPic(q)
#displayPic(quadRecurse(pyTri, gwTri, 2))    
#displayPic(recurseDiag(pyTri, gwTri, 3))  




# #Testing quilt
#for levels in range(5):
#    p = quilt(pyTri, gwTri, 2)
#    displayPic(p)
displayPic(quilt(pyTri, gwTri, 2))
#displayPic(emptyPic)   # addressing issue with cs1graphics: sometimes need to display a simple picture for the earlier complex one to show up!

