#!/usr/bin/python3

#Python code to get parity

n = (input("Enter binary bit data that has to be transmitted= "))
y = int(n)

#Total number of digits in the input data
count = 0
while y!=0:
	y = round(y/10)
	count = count+1
#print("Total bits in the data ", count)

#Convert string to list

bits = [int(d) for d in str(n)]
#print (bits)

#counting number of 1's in the enter binary bit data that has to be transmitted.


count1 = 0
for i in bits:
	if i == 1:
		count1 = count1+1
	else:
		count = count

#adding parity bit in end of the data		
if count1%2 == 0:
	bits.append(1)
	#print(bits)
else:
	bits.append(0)
	#print(bits)

#convert list into string

modifiedstring = ''.join(str(e) for e in bits)		
print("Parity bit data :",modifiedstring)

#The string 0101 is used as the bit string or flag to indicate the end of the frame.
m = "0101"
o = modifiedstring+m
print("Transmitting data: ",o)





