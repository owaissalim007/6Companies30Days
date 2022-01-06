#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here
        start = 1
        st = []
        res = ''
        for i in range(len(S)):
            char = S[i]
            if char == 'D':
                st.append(start)
                start += 1
            else:
                st.append(start)
                start += 1
                while len(st) > 0:
                    res += str(st.pop())
        st.append(start)
        while len(st) > 0:
            res += str(st.pop())
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
