class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归方法，一定从最底层node的情况开始写
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val<=l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        elif l1.val>l2.val:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2

if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)

    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(2)
    l5 = ListNode(5)
    l6 = ListNode(8)
    l4.next = l5
    l5.next = l6

    a = s.mergeTwoLists(l1,l4)
    b = a.next
    c = b.next
    d = c.next 
    print(d.next.val)
