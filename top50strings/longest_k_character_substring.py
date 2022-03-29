# problem: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:

    def longestKSubstr(self, s, K):
        counter = {}
        
        mx = -1
        st = 0
        for en, c in enumerate(s):
            if c not in counter:
                counter[c] = 0
                
            counter[c] += 1
            
            if len(counter.keys()) == K:
                mx = max(mx, sum(counter.values()))
            elif len(counter.keys()) > K:
                
                while len(counter.keys()) > K and st <= en:
                    kicked = s[st]
                    st += 1
                    
                    counter[kicked] -= 1
                    if counter[kicked] == 0:
                        del counter[kicked]
               
        return mx 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends