# Source : https://leetcode.com/problems/add-two-numbers/
# Author : Bohan Shan
# Date   : 2018-02-22

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    1. Finds the sum of the first number(l1) and second number(l2).
    2. Create a new list representing the sum.
    '''
    def addTwoNumbers (self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1;
        sum1 = num1.val;
        num2 = l2;
        sum2 = num2.val;

        # sums first number
        count = 1;
        while(num1.next != None):
            sum1 += num1.next.val * 10**count;
            num1 = num1.next;
            count+=1;
        # sums second number
        count = 1;
        while(num2.next != None):
            sum2 += num2.next.val * 10**count;
            num2 = num2.next;
            count+=1;
        # final sum
        sumfinal = sum1 + sum2;

        #Create list representing sum
        count = 0;
        digit = sumfinal % 10;
        sumfinal /= 10;
        curr = ListNode(digit);
        head = curr;
        while (sumfinal!=0):
            digit = sumfinal % 10;
            sumfinal /= 10;
            prev = curr;
            curr = ListNode(digit);
            prev.next = curr;

        return head;
