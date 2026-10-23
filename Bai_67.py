# import math

# n = int(input())
# print(math.factorial(n))

n = int(input())
 
ket_qua = 1 
for i in range(1, n + 1):
    ket_qua *= i
print(ket_qua)
