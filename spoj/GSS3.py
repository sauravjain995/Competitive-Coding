def kadane(a,size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
         
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far
n = input()
A = map(int,raw_input().split())
for _ in range(input()):
    B = map(int,raw_input().split())
    if(B[0]==1):
        if(B[1]==B[2]):
            print A[B[2]-1]
        else:
            print kadane(A[B[1]-1:B[2]],len(A[B[1]-1:B[2]]))
    elif B[0] == 0:
        A[B[1]-1] = B[2]
