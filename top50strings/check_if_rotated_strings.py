# problem: https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1/?page=1&curated[]=3&sortBy=submissions#


# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        originalWords = S.split(".")
        
        return ".".join(originalWords[::-1])

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends