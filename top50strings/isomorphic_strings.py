# problem: https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1/?page=1&curated[]=3&sortBy=submissions#

#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
            
        mapping = {}
        in_mapping = {}
        for s1, s2 in zip(str1, str2):
            if s1 not in mapping:
                mapping[s1] = s2
            if s2 not in in_mapping:
                in_mapping[s2] = s1
                
            m1, m2 = mapping[s1], in_mapping[s2]
            
            if m1 != s2 or m2 != s1:
                return 0
                
                
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends