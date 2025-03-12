class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_elements = len(nums1) + len(nums2)
        
        is_odd = (total_elements%2 != 0)
        median_loc = (total_elements-1) / 2 if is_odd else (total_elements/2) -1

        n = 0
        result = 0
        while n <= median_loc:
            if not nums1:
                result = nums2.pop(0)
            elif not nums2:
                result = nums1.pop(0)
            elif nums1[0] < nums2[0]:
                result = nums1.pop(0)
            elif nums1[0] > nums2[0]:
                result = nums2.pop(0)
            elif nums1[0] == nums2[0]:
                result = nums1.pop(0)
            n += 1
        
        if is_odd is False:
            if not nums1:
                result += nums2.pop(0)
            elif not nums2:
                result += nums1.pop(0)
            elif nums1[0] < nums2[0]:
                result += nums1.pop(0)
            elif nums1[0] > nums2[0]:
                result += nums2.pop(0)
            elif nums1[0] == nums2[0]:
                result += nums1.pop(0)
            return result/2
        else :
            return result