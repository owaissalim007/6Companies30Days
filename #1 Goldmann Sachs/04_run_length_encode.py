#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    res = ''
    curr_char_run = ''
    run_length = 0
    
    for i in range(len(arr)):
        if i == 0:
            curr_char_run = arr[i]
            run_length = 1
        else:
            curr_char = arr[i]
            if curr_char == curr_char_run:
                run_length += 1
            else:
                res += curr_char_run + str(run_length)
                curr_char_run = curr_char
                run_length = 1
    res += curr_char_run + str(run_length)
    return res

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
