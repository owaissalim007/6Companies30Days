#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        st, ans, n = [], "", ""
        for c in s:
            if c.isalpha():
                ans += c
            elif c.isdigit():
                n += c
            elif c == '[': 
                st.append((n, ans))
                n, ans = "", ""
            else:
                cnt, prev = st.pop()
                ans = prev + ans * int(cnt)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends
