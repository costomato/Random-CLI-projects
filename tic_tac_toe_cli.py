# CLI based tic-tac-toe game by Kaustubh!

def chkline(l):
    if l[4] == l[1] == l[7] or l[4] == l[3] == l[5] or l[4] == l[0] == l[8] or l[4] == l[2] == l[6]:
        return l[4]
    if l[0] == l[1] == l[2] or l[0] == l[3] == l[6]:
        return l[0]
    if l[8] == l[7] == l[6] or l[8] == l[5] == l[2]:
        return l[8]


t = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def printlst(l):
    for i in range(9):
        print("_"+l[i]+('|', '')[i == 2 or i == 5 or i == 8], end='')
        if i == 2 or i == 5 or i == 8:
            print()


p1win, p2win = False, False
p1sign = p2sign = ''

while True:
    p1sign = str(input("Enter the sign of player 1 [e.g.: X]"))
    p2sign = str(input("Enter the sign of player 2 [e.g.: O]"))
    if p1sign != p2sign:
        break
    print("Please use different signs for both the players!")

print("1. Player 1 plays first\n2. Player 2 plays first")
choice = int(input("Enter your choice [press 1 or 2]:"))

while True:
    if choice == 1 or choice == 2:
        break
    choice = int(input("Wrong choice!! Please choose again... [1 or 2]"))

# the game logic begins
for i in range(9):
    print(chr(27)+'[2j')
    printlst(t)
    if chkline(t) == p1sign:
        p1win = True
        break
    if chkline(t) == p2sign:
        p2win = True
        break
    print("Enter the place of player", choice, "sign [1~9]")
    n = int(input())
    while True:
        if n > 9 or n < 1 or t[n-1] == p1sign or t[n-1] == p2sign:
            n = int(input("Wrong place! Please enter again... [1-9]"))
        else:
            break
    t[n-1] = (p1sign, p2sign)[choice == 2]
    choice = 3-choice

if p1win:
    print("Player 1:", p1sign, "wins!")
elif p2win:
    print("Player 2:", p2sign, "wins!")
else:
    print("MATCH DRAW!")
