# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : Bohan Shan
# Date   : 2018-02-22

'''

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
 must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    '''
    Finds substring by maintaining a list of chars used
    and incrementing a variable max_length.
    '''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = list(s)
        chars = list();
        length = 0;
        max_length = 0;
        ind = 0;
        for char in arr:
            if char in chars:
                #Looking for repeat char and deleting chars before
                ind = chars.index(char);
                length-=(ind+1);
                chars = chars[ind+1:];
            #Add char to list and length
            chars.append(char);
            length+=1;
            #Update max_length
            if(length > max_length):
                max_length = length;
        return max_length
