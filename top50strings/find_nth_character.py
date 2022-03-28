# Problem: https://practice.geeksforgeeks.org/problems/find-the-n-th-character5925/1/?page=1&curated[]=3&sortBy=accuracy#

#User function Template for python3

class Solution:
    transCache = None
    def nthCharacter(self, S, R, N):
        characterNum = 1<<R 
        originalCharacter = N // characterNum
        characterIndex = N % characterNum
        
        lastIterationCharacters = self.transform(S[originalCharacter], R)
        return lastIterationCharacters[characterIndex]
    
    def transform(self, S, R):
        if self.transCache:
            return self.transCache[(S, R)]
        
        self.transCache = {}
        # (character, R)
        self.transCache[("1", 0)] = "1"
        self.transCache[("0", 0)] = "0"
        
        r = 1
        while r <= 20:
            self.transCache[("1", r)] = self.transCache[("1", r-1)] + self.transCache[("0", r-1)]
            self.transCache[("0", r)] = self.transCache[("0", r-1)] + self.transCache[("1", r-1)]
            r+=1
        
        
        return self.transCache[(S, R)]
        
        
        
    # 10001 --> 5 
    # Setiap iterasi: len * 2 (karena setiap karakter akan jadi 2 karakter)
    # 10 01 01 01 10 --> 10
    # Iterasi: 2 --> 20
    # 1001 0110 0110 0110 1001
    
    # R = 2 --> N = 7 (1 karatker, 4 karakter) -> 1
    # Iterasi: 3 --> 40
    
    # Total Panjang: len(string awal) * 2^(R)
    
    # Ambil 1 karakter: "1" -- "0" 
    # Iterasi 1 --  2 --> "10" -- "01"
    # Iterasi 2 --  4 --> "1001" -- "0110"
    
    # Iterasi ke R: total karakter setiap karakter asli: 2^R
    
    # Kalau kita mau tau digit ke N:
    # N/(2^R) -- p --> ini: kita bakal tahu digit ke N, adalah 
    # turunannya digit ke P pada karakter asli.
    # N%(2^R) -- q --> digit ke berapa pada turunan
    # R = 3x
    # N = 9
    
    #iter0: 1 -- 0
    #1: 10 -- 01
    #2: 10_01 -- 01_10
    #3: 1001_0110 -- 0110_1001
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends