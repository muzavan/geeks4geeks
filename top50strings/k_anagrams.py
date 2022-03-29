# problem: https://practice.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1/?page=1&curated[]=3&sortBy=accuracy#

#User function template for Python 3

class Solution:
    def areKAnagrams(self, str1, str2, k):
        # code here
        if len(str1) != len(str2):
            return False
            
        str1_counter = {}
        for c in str1:
            if c not in str1_counter:
                str1_counter[c] = 0
            str1_counter[c] += 1
            
        total = len(str2)
        for c in str2:
            if c in str1_counter and str1_counter[c] > 0:
                str1_counter[c] -= 1
                total -= 1
                
                
        return total <= k

#{ 
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends