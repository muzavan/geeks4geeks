# problem: https://practice.geeksforgeeks.org/problems/decode-the-pattern1138/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:

    def lookandsay(self, n):
        # code here
        return self.lookandsayfrom("1", n)
    
    def lookandsayfrom(self, prev, n):
        if n == 1:
            return prev
        
        
        prev_num = prev[0]
        cntr = 1
        i = 1
        result = []
        while i < len(prev):
            curr = prev[i]
            if curr != prev_num:
                result.extend([cntr, prev_num])
                cntr = 1
                prev_num = curr
            else:
                cntr += 1
            i += 1
            
            
        result.extend([cntr, prev_num])
            
        return self.lookandsayfrom("".join([str(digit) for digit in result]), n - 1)
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends