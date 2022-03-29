# problem: https://practice.geeksforgeeks.org/problems/closest-strings0611/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    def shortestDistance(self, s, word1, word2):
        # code here
        idx1 = []
        idx2 = []
        
        for i, word in enumerate(s):
            if word == word1:
                idx1.append(i)
            if word == word2:
                idx2.append(i)
                
        min_dst = len(s)        
        for i in idx1:
            for j in idx2:
                min_dst = min(min_dst, abs(i-j))
                
                
        return min_dst

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        s = list(map(str,input().split()))
        word1 = input()
        word2 = input()
        ob = Solution()
        ans = ob.shortestDistance(s, word1, word2)
        print(ans)

# } Driver Code Ends