# problem: https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        romanMap = {
            "M" : 1000,
            "CM" : 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        
        i = 0
        tot = 0
        while i < len(S):
            if i < len(S) - 1:
                poss = S[i:i+2]
                if poss in romanMap:
                    tot += romanMap[poss]
                    i += 2
                    continue
                
            poss = S[i]
            tot += romanMap[poss]
            i += 1
            
        return tot
                
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends