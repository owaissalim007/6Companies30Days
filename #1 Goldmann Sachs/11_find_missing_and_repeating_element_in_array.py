#User function Template for python3

class Solution:
    def sumOfSquare(self, arr):
        s = 0
        for ele in arr:
            s += ele**2
        return s
    
    def findTwoElement(self, arr, n): 
        # code here
        res = [0]*2
        sum_1toN = sum(range(n+1))
        sum_given = sum(arr)
        sum_sq_1toN = self.sumOfSquare([i for i in range(1,n+1)])
        sum_sq_given = self.sumOfSquare(arr)
        const1 = sum_1toN - sum_given
        const2 = (sum_sq_1toN - sum_sq_given)//const1
        res[0] = (const2-const1)//2
        res[1] = (const2+const1)//2
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
