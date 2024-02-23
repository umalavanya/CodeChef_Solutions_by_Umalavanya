# 500 Average

T = int(input())
for i in range(T):
    A,B,C = map(str,input().split())
    A,B,C = int(A),int(B),int(C)
    if A+B > (2*C):
        print("Yes")
    else:
        print("No")
