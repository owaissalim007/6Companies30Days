class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(m, n):
            while n:
                m, n = n, m % n
            return m
        n1, n2 = len(str1), len(str2)
        l = gcd(n1, n2)
        result = str1[:l]
        if result * (n1 // l) == str1 and result * (n2 // l) == str2:
            return result
        else:
            return ""
