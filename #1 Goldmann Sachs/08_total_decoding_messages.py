#User function Template for python3

class Solution:
	def CountWays(self, str):
		# Code here
		if len(str) == 0:
            return 1
        if str[0] == '0':
            return 0
		n = len(str)
		p = q = res = 1
		for i in range(1, n):
		    t = (int(str[i-1])-0)*10 + int(str[i]) - 0
		    if t >= 10 and t <= 26:
		        if t == 10 or t == 20:
		            res = p
	            else:
	                res = p + q
	        else:
	            if t % 10 == 0:
	                return 0
	            else:
	                res = q
	        p = q
	        q = res
        return res % (10**9 + 7)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends
