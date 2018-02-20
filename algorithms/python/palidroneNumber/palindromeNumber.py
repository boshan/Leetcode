class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x);
        digits = len(num);
        pali = True;
        if (x < 0):
            pali = False;
        while (digits > 1 and pali):
            lsb = int(num[0]);
            msb = int(num[digits-1]);
            if (lsb != msb):
                pali = False;
            if (digits > 2):
                num = num[1:digits-1];
            digits -= 2;

        return pali
