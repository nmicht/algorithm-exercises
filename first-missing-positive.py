# INCOMPLETE
# https://leetcode.com/submissions/detail/211630040/

def solution(A):
    # write your code in Python 3.6
    A.sort()
    size = len(A)

    if size == 0:
        return 1
    if A[0] > 1:
        return 1

    smallest = 0
    
    for i in range(0, size - 1):
        if A[i] == A[i+1] or A[i]+1 == A[i+1]:
            continue
        else:
            smallest = A[i]+1
    
    if smallest == 0:
        return A[-1] + 1

    if smallest < 0:
        return 1

    return smallest


print(solution([-1, -100, -3, -5, -1, 0, -3]))
