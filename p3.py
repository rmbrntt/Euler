__author__ = 'Ryan'
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

n = 13195
prime_list = []

largest_prime = 0

#while largest_prime == 0:

for num in range(2, n):
    if n % num == 0:
        prime_list.extend([num])
        print prime_list



