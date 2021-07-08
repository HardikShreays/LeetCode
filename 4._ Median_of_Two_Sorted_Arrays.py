class Solution:
  '''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).'''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def mergeList(a, b):
            sorted_list = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i]<=b[j]:
                    sorted_list.append(a[i])
                    i += 1
                else:
                    sorted_list.append(b[j])
                    j += 1
            while j < len(b):
                sorted_list.append(b[j])
                j += 1
            while i < len(a):
                sorted_list.append(a[i])
                i += 1

            return sorted_list
        lis = mergeList(nums1, nums2)
        lenght = len(lis)
        if lenght%2==0:
            median = (lis[lenght//2]+lis[(lenght//2)-1])/2
            return median
        return lis[lenght//2]

