# Merged K sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/?source=submission-noac
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        def _smallest_number_of_element(lists):
            min_el = 10001
            min_l = 0
            
            for i, l in enumerate(lists):
                if not l:
                    lists.remove(l)
                    continue
                if l.val < min_el:
                    min_el = l.val
                    min_l = i
            if lists and lists[min_l]:
                if lists[min_l].next == None:
                    lists.pop(min_l)
                else:           
                    lists[min_l] = lists[min_l].next
                return ListNode(min_el, None)
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0] if lists[0] else None
        
        result = _smallest_number_of_element(lists)
        head = result
        while lists:
            min_ele = _smallest_number_of_element(lists)
            if not min_ele:
                break
            result.next = min_ele
            result = result.next
        return head
