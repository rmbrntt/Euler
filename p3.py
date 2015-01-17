__author__ = 'Ryan'
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
import math
n = 600851475143
num_list = []
prime_list = []

#### Overflow error, range too large for memory
# for num in range(2, n):
#     if n % num == 0:
#         print 'current number that can be divided into the input:', num
#         for nums in range(1, num+1):
#             print 'checking if', num, 'is divisble by', nums
#             if num % nums == 0:
#                 num_list.extend([nums])
#                 print 'adding', nums, 'to the temporary number list'
#                 print 'temporary number list:', num_list
#         if len(num_list) == 2:
#             prime_list.extend([num])
#             print 'prime list extended', prime_list
#             print num
#         num_list = []
#
# print 'max prime:', max(prime_list)

for num in range(2, int(math.sqrt(n))+2):
    if n % num == 0:
        for nums in range(1, num+1):
            if num % nums == 0:
                num_list.extend([nums])
        if len(num_list) == 2:
            prime_list.extend([num])
        num_list = []
print 'Max prime:', max(prime_list)



