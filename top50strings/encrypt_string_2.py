# problem: https://practice.geeksforgeeks.org/problems/encrypt-the-string-21117/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    def encryptString(self, S):
        # code here
        result = []
        counter = 1
        prev = S[0]
        i = 1
        while i < len(S):
            curr = S[i]
            i+= 1
            if curr == prev:
                counter += 1
                continue
            
            result.append(prev)
            result.append(self.to_hex(counter))
            prev = curr
            counter = 1
            
        result.append(prev)
        result.append(self.to_hex(counter))
        
        return "".join(result[::-1])
    
    def to_hex(self, n):
        result = []
        hex_map = {
            10: "a",
            11: "b",
            12: "c", 
            13: "d", 
            14: "e", 
            15: "f",
        }
        
        while n > 0:
            rem = n % 16
            if rem in hex_map:
                result.append(hex_map[rem])
            else:
                result.append(str(rem))
            n = n // 16
        
        return "".join(result[::-1])

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.encryptString(S))
# } Driver Code Ends