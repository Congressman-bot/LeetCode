class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # If no string is entered then none
        if not s:
            return ""
        
        # Create a tracker for the longest palindrome found 
        longest = ""
        
        # Helper function to search from the middle of the string going outwards
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            # Return palindrome
            return s[left + 1:right]
        
        for i in range(len(s)):
            # Odd string center in 'dad' is 'a'
            p1 = expand(i, i)
            
            # Even string center in 'abba' is like 'bb'
            p2 = expand(i, i + 1)
            
            # The longest between p1 and p2 becomes the longest palindrome
            current_max = p1 if len(p1) > len(p2) else p2
            
            # Update the value of longest if the current_max palindrome is longer
            if len(current_max) > len(longest):
                longest = current_max
                
        return longest
                
solution = Solution()
#  Prompt the user to enter a string
value = input("Enter string: ")
print(solution.longestPalindrome(value))