# problem: https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        s_arr = sorted(arr, key=lambda el: len(el))
        if len(s_arr) == 0:
            return "-1"
            
        if len(s_arr) == 1:
            return s_arr[0]
            
        prefix = s_arr[0]
        idx = 1
        
        while idx < n:
            curr = s_arr[idx]
            
            while len(prefix) > 0 and curr[:len(prefix)] != prefix:
                prefix = prefix[:-1]
            
            if len(prefix) == 0:
                return "-1"
            idx += 1
            
        
        return prefix

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends