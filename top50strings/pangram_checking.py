# problem: https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1/?page=1&curated[]=3&sortBy=submissions

#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        allset = set('abcdefghijklmnopqrstuvwxyz')
        s = s.lower()
        for ss in s:
            if ss in allset:
                allset.remove(ss)
            
        return 1 if len(allset) == 0 else 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends