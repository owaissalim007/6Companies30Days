#User function Template for python3

class Solution:
    def canPair(self, nums, k):
        # Code here
        hmap = {i:0 for i in range(k)}
        for el in nums:
            temp = el % k
            hmap[temp] += 1
        for i in range(k):
            if i == 0:
                if hmap[i] % 2 == 1:
                    return False
            else:
                if (i + (i % k)) == 0:
                    if hmap[i] % 2 == 1:
                        return False
                else:        
                    if hmap[i] != hmap[k-i]:
                        return False
        return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends
