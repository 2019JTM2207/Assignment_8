#!/usr/bin/python3

print("Welcome to the Game!")
c = 0
if c == 0:
	print("Player 1's chance")
	c = c+1
else:
	print("Player 2's chance")
	c= c-1

print("Enter the position : ",end="")
position = int(input())
print("Enter the number : ",end="")
number = int(input())

#check for constraints
if position >=1 and position <=9:
	if number >=1 and number <=9:	
		print("Both position and number are valid")
	else:
		print("Number is invalid")
else:
	print("Position is invalid")


#draw 3X3 Numeric Tic-Tac-Toe
def drawboard(board):
    print ('    |   |   ')
    print ('' +board[6]+ '    | ' +board[7]+ '  |   ' +board[8] )
    print ('    |   |   ')
    print ('--------------')
    print ('    |   |   ')
    print ('' +board[3]+ '    | ' +board[4]+ '  | ' +board[5] )
    print ('    |   |   ')
    print('--------------')
    print ('    |   |   ')
    print ('' +board[0]+ '    | ' +board[1]+ '  |' +board[2] )
    print ('    |   |   ')

drawboard(['', '', '', '', '', '', '', '', ''])


