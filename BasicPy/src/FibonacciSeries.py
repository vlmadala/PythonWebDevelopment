# Fibonacci Series :
# the sum of two elements defines the next number of the series
import sys
print(sys.version)

a = int(input("Enter the first number of the series")) # First in the series
b = int(input("enter the second number of the setries")) #Second number in the series
n = int(input("ENter the number of terms needed"))
print(a,b, en =", ")
while (n-2):
	c = a + b  # c =0+1 = 1
	a = b       # a =1
	b = c		# b=1
	print(c)
	n = n-1