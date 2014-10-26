__author__ = 'barnett.io'
fib = 1
a = 1
b = 0
even_fib = 0

while fib < 4000000:
    print 'Currently on Fibonacci #'+ str(fib)
    fib = a+b
    b = a
    a = fib
    if fib % 2 == 0:
        even_fib += fib
print "The sum of all even Fibonacci numbers with values less than 4 million: " + str(even_fib)