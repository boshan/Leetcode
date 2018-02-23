# Source : https://leetcode.com/problems/palindrome-number/
# Author : Bohan Shan
# Date   : 2018-02-22
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution(object):
    '''
    Checks if a number is a paladrome.
    Returns false on negative numbers.
    '''
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x);
        digits = len(num);
        pali = True;
        # negative numbers returns false
        if (x < 0):
            pali = False;
        # checks equality of integers forwards and back.
        while (digits > 1 and pali):
            lsb = int(num[0]);
            msb = int(num[digits-1]);
            if (lsb != msb):
                pali = False;
            if (digits > 2):
                num = num[1:digits-1];
            digits -= 2;

        return pali
