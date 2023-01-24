#!/usr/bin/python
def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c in sublist:
            return (i, sublist.index(c))
    return -1, -1
    
def displayPathtoPrincess(n,grid):
    # find the position of 'm'
    m0, m1 = in_list('m', grid)
    # find the position of 'p'
    p0, p1 = in_list('p', grid)
    # for UP and DOWN moves
    updown = m0-p0
    print((("DOWN\n", "UP\n")[updown > 0]) * abs(updown), end='')
    
    # for LEFT and RIGHT moves
    lr = p1-m1
    print((("LEFT\n", "RIGHT\n")[lr > 0]) * abs(lr), end='')
        

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

'''
PROBLEM STATEMENT

Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input

3
---
-m-
p--
Sample output

DOWN
LEFT
'''