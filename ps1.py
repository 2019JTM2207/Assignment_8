#!/usr/bin/python3

#Python code to get parity

n = (input("Enter binary bit data that has to be transmitted= "))
y = int(n)

#Total number of digits in the input data
count = 0
while y!=0:
	y = round(y/10)
	count = count+1
print("Total bits in the data ", count)

#Convert string to list

digits = [int(d) for d in str(n)]
print (digits)

c1 = 0
c2 = 0

for i in digits:
	if i == 1:
		c1 = c1+1
	else:
		if c1/2 == 0:
			digits.append('1')
			print(digits)
		else:
			print(digits)
			
word = n
print(split(word)) 

#The string 0101 is used as the bit string or flag to indicate the end of the frame.
m = "0101"
o = n+m
print(o)
x = "010" in n
print(x)
z = n.index("010")
print(z)




