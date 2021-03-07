def add_binary_arrays(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, 0, -1):
        res = A[i] + B[i] + carry
        C[i + 1] = res % 2
        carry = res // 2
    C[0] = carry
    return C

# 2 as binary array
A = [0, 0, 1, 0]
# 3 as binary array
B = [0, 0, 1, 1]
print("A =    " + str(A))
print("B =    " + str(B))
print("C = " + str(add_binary_arrays(A, B)))