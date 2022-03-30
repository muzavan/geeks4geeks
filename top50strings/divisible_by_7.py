# problem: https://practice.geeksforgeeks.org/problems/divisible-by-73224/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    def isdivisible7(self, num):
        curr_digits = 0
        for digit in num:
            curr_digits = curr_digits * 10 + int(digit)
            curr_digits = curr_digits % 7
        
        return 1 if curr_digits == 0 else 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        ob=Solution()
        print(ob.isdivisible7(s))
# } Driver Code Ends