'''
Created on 22-Jul-2018

@author: vijaya
'''
def fib():
    a , b =0 , 1
    start =int(input("Please input the desired number"))
    for i in range(start):
        b = a +b
        a = b 
        