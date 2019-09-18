#!/usr/bin/python3

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 

print("Welcome to the Game!")
player = 0

count = 0
while count < 1:

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

	#check for whether it is Player 1’s or Player 2’s chance.

	if player == 0:
		print("Player 1's chance")
		player = player+1
	else:
		print("Player 2's chance")
		player = player-1

	 
	# Function for Draws Game Board    
	def DrawBoard():    
	    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
	    print("___|___|___")    
	    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
	    print("___|___|___")    
	    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
	    print("   |   |   ")  

	DrawBoard()  

	# Function for Checks position is empty or not    
	def CheckPosition(x):    
		if(board[x] == ' '):    
			return True    
		else:    
			return False    

	print ('The count is:', count)
	count = count + 1

