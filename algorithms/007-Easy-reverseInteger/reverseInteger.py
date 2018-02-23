# Source : https://leetcode.com/problems/reverse-integer/
# Author : Bohan Shan
# Date   : 2018-02-22

class Solution(object):
    '''
    Reversed the numbers using different cases
    '''
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x;
        new_num = 0;

        #if not 32-bit int return 0
        if (num > 2147483647 or num < -2147483648):
            return 0;

        #If negative, treat the number
        if (num < 0):
            num *= -1;

        #creates new int by way of least significant bit.
        while (num > 0):
            new_num *= 10;
            new_num += num%10;
            num/=10;

        if (x < 0):
            new_num *= -1;

        #reversed number must be 32-bit int or return 0
        if (new_num > 2147483647 or new_num < -2147483648):
            return 0;

        return new_num;
