# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):



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

        count = 1;
        while(num1.next != None):
            sum1 += num1.next.val * 10**count;
            num1 = num1.next;
            count+=1;

        count = 1;
        while(num2.next != None):
            sum2 += num2.next.val * 10**count;
            num2 = num2.next;
            count+=1;

        sumfinal = sum1 + sum2;

        #This creates the new list
        count = 0;
        #Create head;
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
        
