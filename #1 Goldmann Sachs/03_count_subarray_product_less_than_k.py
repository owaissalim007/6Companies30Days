#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        if not a:
            return 0
        j = 0
        res = 1
        count = 0
        for i in range(n):
            res *= a[i]
            if res >= k:
                while j <= i and res >= k:
                    res /= a[j]
                    j += 1
            count += i - j + 1
        return count
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
