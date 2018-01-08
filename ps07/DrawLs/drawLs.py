# Isabel Staccuneddu
# PSet 7
# *~Turtles~*
# March 15th, 2016

from turtle import *
import time

#  ----------write your code here -----------

def drawOne(size): #Helper function
    """draws one L with the longest side being of size length"""
    fd((float(2.)/float(3.))*size)
    lt(90)
    fd(size/3)
    lt(90)
    fd(size/3)
    rt(90)
    fd((float(2.)/float(3.))*size)
    lt(90)
    fd(size/3)
    lt(90)
    fd(size)
    lt(90) #turtle ends facing right

def drawLs(size, level):
    if level == 0:
        pass
    else:
        drawOne(size) #draw initial L
        pu()        #positions turtle appropriately to drawLs
        lt(90)
        fd(size)
        rt(90)
        pd()
        drawLs(size/2., level-1)  #first recursive call
        pu()        #positions turtle again to drawLs
        #Turtle at upper left hand corner of topmost L facing right
        rt(90)
        fd(size)
        lt(90)
        fd(size*2*float(1./3.))
        pd()
        drawLs(size/2., level-1)  #second recursive call

        

# --------------------------------------------
     
def initialize_turtle():
    setup(800,600) # Create a turtle window 
    reset() # Show turtle window and turtle
    pencolor('red')
    speed(25) # can change this to vary the speed of your turtle
    shape("turtle") # Make turtle shape a turtle (as opposed to arrow)
    #Turtle, by default, starts roughly in center of canvas
    pu()
    # Put turtle in bottom left cornerish to better fit the L pattern
    setx(-200)
    sety(-200)
    pd()
    # Magical statements to make turtle window come to top of screen.
    getscreen()._root.attributes('-topmost', True)
    getscreen()._root.attributes('-topmost', False)
    


def run():
    initialize_turtle()
    drawLs(100,3)
    #exitonclick()
   
run() #Opens 2 different windows