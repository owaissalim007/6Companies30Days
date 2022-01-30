#User function Template for python3

class Solution:
    def find3number(self, A, n):
        # code here
        low = 0
        high = n-1
        small = [0]*n
        small[0] = -1
        for i in range(1, n):
            if arr[i] <= arr[low]:
                low = i
                small[i] = -1
            else:
                small[i] = low
        great = [0]*n
        great[n-1] = -1
        for i in range(n-2, -1, -1):
            if arr[i] >= arr[high]:
                high = i
                great[i] = -1
            else:
                great[i] = high
        res = []
        for i in range(n):
            if small[i] != -1 and great[i] != -1:
                res.append(A[small[i]])
                res.append(A[i])
                res.append(A[great[i]])
                return res
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, res, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==res[m-1]:
        return isSubSeq(arr, res, n-1, m-1)
    return isSubSeq(arr, res, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    res = Solution().find3number(arr, n)
    # print(res)
    # print(isSubSeq(arr, res, n, len(res)))
    if len(res)!=0 and len(res)!=3:
        print(-1)
        continue
    if len(res)==0:
        print(0)
    elif res[0]<res[1] and res[1]<res[2] and isSubSeq(arr, res, n, len(res)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends
