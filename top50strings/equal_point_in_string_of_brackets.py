# problem: https://practice.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1/?page=3&curated[]=3&sortBy=submissions

#User function Template for python3

class Solution:
    def findIndex(self,astr):
        # Your code goes here
        closing = sum([1 for a in astr if a == ")" ])
        opening = 0
        
        idx = 0
        while idx < len(astr):
            if closing == opening:
                return idx
                
            curr = astr[idx]
            if curr == "(":
                opening += 1
            if curr == ")":
                closing -= 1
            idx += 1
        
        if closing == opening:
            return idx
            
        return -1
        
        # (())))( --> BK: 0 , TP: 4
        # 0: ( --> BK: 1, TP: 4
        # 1: ( --> BK: 2, TP: 4
        # 2: ) --> BK: 2. TP: 3
        # 3: ) --> BK: 2. TP: 2
        # 4 --> Index ke 4
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        str = input()
        ob=Solution()
        print(ob.findIndex(str))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends