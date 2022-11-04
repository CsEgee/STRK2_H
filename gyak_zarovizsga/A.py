def solution(A):
    A.sort()
    i = 0
    for i in range(len(A)):
        if A[i] == i + 1:
            i = i + 1
        else:
            break
    print(i+1)


A = [7, 2, 5, 9, 4, -1, 1]
# A.sort()
# i = 0
# for i in range(len(A)):
#     print(A[i])
solution(A)
