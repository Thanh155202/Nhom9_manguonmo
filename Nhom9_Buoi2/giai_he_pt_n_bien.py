import numpy as np

# Nhập số biến và số phương trình
n = int(input("Nhập số biến (n): "))
m = int(input("Nhập số phương trình (m): "))

# Nhập ma trận hệ số A
A = np.zeros((m, n))
print("Nhập ma trận hệ số A:")
for i in range(m):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))

# Nhập vector b
b = np.zeros(m)
print("Nhập vector b:")
for i in range(m):
    b[i] = float(input(f"b[{i+1}]: "))

# Tính hạng của ma trận hệ số A và ma trận mở rộng
    rank_A = np.linalg.matrix_rank(A)
    augmented_matrix = np.column_stack((A, b))
    rank_augmented_matrix = np.linalg.matrix_rank(augmented_matrix)

# Kiểm tra xem hệ có vô số nghiệm hay không
if rank_A == rank_augmented_matrix and rank_A < n:
    print("Hệ phương trình có vô số nghiệm.")
elif rank_A == rank_augmented_matrix and rank_A == n:
    x = np.linalg.solve(A, b)
    print("Nghiệm của hệ phương trình:")
    for i in range(n):
        print(f"x{i+1} =", x[i])
else:
    print("Hệ phương trình vô nghiệm.")
