# Sort array
A = [1,5,6,7,8,3,4,2]
for i in range (len(A)):
    for j in range(i+1,len(A)):
        if A[i] > A[j]:
            A[i],A[j]=A[j],A[i]
print(A)