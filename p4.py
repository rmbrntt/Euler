__author__ = 'ryan@barnett.io'
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


def largest_palindrome(n_digits):
    three_dig_num_a = range(1, int('1'+str(0)*n_digits))
    three_dig_num_b = range(1, int('1'+str(0)*n_digits))
    largest_product = 0
    for numA in three_dig_num_a:
        for numB in three_dig_num_b:
            current_product = numA * numB
            if str(current_product) == str(current_product)[::-1] and current_product > int(largest_product):
                    largest_product = current_product
    return largest_product