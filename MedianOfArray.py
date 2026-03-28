class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the arrays first
        merged_array = nums1 + nums2
        
        #  Sort the merged arrays
        sorted_array = sorted(merged_array)
        
        # Get the length of the sorted array
        n = len(sorted_array)

        # Find the mid of the length of the sorted array and divide it by 
        # 2 then round of to the nearest whole number
        mid = n // 2

        # if the length of sorted array is even 
        if n % 2 == 0:
            # Get the mean of the mid and it's predecessor
            return (sorted_array[mid - 1] + sorted_array[mid]) / 2.0
        else:
            return float(sorted_array[mid])

# Create an object solution  
solution = Solution()

# Output the result by passing two arguments to the function
print(solution.findMedianSortedArrays([1, 3], [2]))
