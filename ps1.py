#!/usr/bin/python3

# Python code to get parity. 
  
# Function to get parity of number n.
  
# It returns 1 if n has odd parity,
  
# and returns 0 if n has even parity 
def getParity( n ): 
	parity = 0
	while n: 
		parity = ~parity 
		n = n & (n - 1) 
		return parity 
  
#program to test getParity() 
print("Enter binary bit data that has to be transmitted.")
n = int(input())
print ("Parity of no ", n," = ", ( "odd" if getParity(n) else "even")) 
