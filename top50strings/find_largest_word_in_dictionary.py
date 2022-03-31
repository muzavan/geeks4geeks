# problem: https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1/?page=2&curated[]=3&sortBy=accuracy#

#User function Template for python3
class Solution:
    def findLongestWord (self, S, d):
        # code here 
        
        max_word = ""
        for word in d:
            if self.match(S, word):
                max_word = self.select_max_word(max_word, word)
                
        return max_word
        
    def match(self, goals, word):
        iw = 0
        ig = 0
        
        if len(word) > len(goals):
            return False
        
        while iw < len(word):
            while ig < len(goals) and word[iw] != goals[ig]:
                ig += 1
                
            if ig >= len(goals):
                return False
                
            iw += 1
            ig += 1
            
        return True

        # ale, apple, monkey
        
        # abpcplea
        # a --> (ale, apple)
        # b --> 
        # p --> (pple, plea)
        # c -->
        # p --> (ple, plea)
        # l --> (le, lea)
        # e --> (e, ea)
        # a --> (a)
        
        
        
    # Works, but maybe not the best
    #     unique_char = set(S)
    #     d = set(d)
    #     for word in list(d):
    #         for w in word:
    #             if w not in unique_char and word in d:
    #                 d.remove(word)
        
    #     poss = {}
    #     for word in d:
    #         # (a) - > [(le, apple), (le, 3)]
    #         initial = word[0]
    #         if initial not in poss:
    #             poss[initial] = {}
    #         if word not in poss[initial]:
    #             poss[initial][word] = word
            
    #     max_word = ""
    #     for s in S:
    #         if s in poss:
    #             all_poss_word = poss[s]
    #             for rem_word, word in list(all_poss_word.items()):
    #                 if len(rem_word) == 1:
    #                     max_word = self.select_max_word(max_word, word)
    #                     continue
                    
    #                 new_rem_word = rem_word[1:]
    #                 initial = new_rem_word[0]
                    
    #                 if initial not in poss:
    #                     poss[initial] = {}
                        
    #                 if new_rem_word not in poss[initial]:
    #                     poss[initial][new_rem_word] = word
    #                 else:
    #                     poss[initial][new_rem_word] = self.select_max_word(word, poss[initial][new_rem_word])
                
    #     return max_word
        
    def select_max_word(self, word1, word2):
        if len(word1) > len(word2):
            return word1
        if len(word2) > len(word1):
            return word2
            
        if word1 < word2:
            return word1
        return word2


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n = int(n)
        d = input().split()
        for itr in range(n):
            d[itr] = d[itr]
        S = input()

        ob = Solution()
        print(ob.findLongestWord(S, d))

# } Driver Code Ends