# TernaryBalance
## Problem
A simple class to weigh - on a balance with 2 cups - a given integer value using a ternary weight set:
1,3,9,27,81,243,..

Input (on the command line) should be a valid integer value
If there is no valid integer value input on the command line then the default value of 100 will be used.

The output will be a text string of the form:

To weigh 100 in right cup of balance, one needs to place the ternary weights in the left (L) and right (R) cups as follows -
L: 81
L: 27
R: 9
L: 1

This is to represent the balance in the state:

       \81,27,1/      \100, 9/
    
