# problem: https://practice.geeksforgeeks.org/problems/convert-to-roman-no/1/?page=1&curated[]=3&sortBy=accuracy#

#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        rom = []
        while n > 0:
            limit, char = self.selectRoman(n)
            rom.append(char)
            n -= limit
        return "".join(rom)
        
    def selectRoman(self, n):
        selection = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
            (0, ''),
        ]
        
        for limit, char in selection:
            if n >= limit:
                return limit, char
                
        assert False

#{ 
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends