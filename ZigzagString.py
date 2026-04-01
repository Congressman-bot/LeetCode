class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Creating of multiple buckets or substrings to hold the strings
        rows = [''] * numRows 
        
        # Initialize the current row as 0
        current_row = 0
        
        going_down = False
        
        # Loop through each character in the string
        for char in s:
            # Add a each character to the respective row
            rows[current_row] += char
            
            # If the 1st or last row going_down = True
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # If going_down=False we move to row 0 else we move to the next row
            current_row += 1 if going_down else -1
        
        return ''.join(rows)
    
sol = Solution()
print(sol.convert('PAYPALISHIRING', 4))
            
        