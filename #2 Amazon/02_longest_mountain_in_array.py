class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maximum = 0
        go_up = 0
        go_down = 0
        
        for idx in range(1, len(arr)):
            
            if (go_down and arr[idx-1] < arr[idx]) or arr[idx-1] == arr[idx]:
                go_up = 0
                go_down = 0
                
            if arr[idx-1] < arr[idx]:
                go_up += 1
            
            if arr[idx-1] > arr[idx]:
                go_down += 1
                
            if go_up and go_down:
                maximum = max( maximum, go_up + go_down + 1 )
                
        return maximum
