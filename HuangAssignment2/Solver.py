# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:46:15 2019
@author: hanks
"""

##  This method is called from Boards.py -- the two inputs are
##    -- initial cell assignments, a list of length N where N is 
##       the problem size (number of rows = number of columns = number
##       of streams = length of each stream).  For example, for a game
##       of size three,  this assigns the value i to the cells on 
##       the diagonal:   [[1,0,0], [0,2,0], [0,0,3]]   -- the value
##       of 0 means the initial value for that cell should be unassigned
##
##    -- streams:  a list of length N, each element is a stream, which 
##       is a list of N coordinates.  For example for N=3:
##          [[(1,1), (2,2), (1,3)], [(1,2), (2,3), (3,3)], [(2,1), (3,1), (3,2)]]
##       Notice that every legal coordinate appears in a stream exactly
##       once, and that the streams are "contiguous" in the sense that 
##       every coordinate is connected to another coordinate either by
##       a row, a column or a diagonal
##
##  Indexing convention:  (row, col) where (1,1) is at the upper left, 
##    (1,2) is one to the right, (2,1) is one down, and (N,N) is at the 
##    upper left
##
##  The return value is exactly the return value from the Python constraints library method
##   getSolutions -- a list of solutions;  each solution is a dictionary 
##   with a key being a coordinate and the value being a value assigned
##   to the cell with that coordinate

from constraint import *

def solveProblem(inits, streams):
    # When you actually solve a CSP, use this code, which calls the Python constraints library
    problem = Problem()
    buildSolution(inits, streams, problem)
    return problem.getSolutions()
    #return dummyExampleNonSolution(len(inits))

def addEqualsConstraint(problem, coord, value):
    problem.addConstraint(lambda x: x == value, [coord])

def buildSolution(inits, streams, problem):
    size = len(inits)    
    variables = [(i+1,j+1) for i in range(size) for j in range(size)]
    problem.addVariables(variables, range(1,size+1)) # every variable is a tuple (x,y)

    for i in range(size): # for row constraint        
        problem.addConstraint(AllDifferentConstraint(),[(j+1,i+1) for j in range(size)]);

    for i in range(size): # for column constraint    
        problem.addConstraint(AllDifferentConstraint(),[(i+1,j+1) for j in range(size)]);    

    for i in range(size): # for stream constraint  
        problem.addConstraint(AllDifferentConstraint(),streams[i]);

    for i in range(size): # for default value constraint
        for j in range(size):
            if inits[i][j] != 0:
                addEqualsConstraint(problem, (j+1,i+1), inits[i][j]) # need to reverse the dimensions between inits and variables            

##  DO NOT COPY THIS CODE!  It is not a solution, it is just 
##  an exmaple and will make the GUI work.  It assigns the value 1
##  to every cell in the problem, which is why it does not need
##  the problem or the inits or the streams
    
def dummyExampleNonSolution(size):
    nonSolution = {}
    for i in range(1, size+1):
        for j in range(1, size+1):
            nonSolution[(i,j)] = 1
    return [nonSolution]