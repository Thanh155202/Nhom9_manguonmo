import numpy as np

# Nhập số phương trình và số ẩn (n) từ người dùng
n = int(input("Nhập số phương trình và số ẩn (n): "))
while (n < 2) :
    # tại đây bắt buộc phải bằng 2, nếu <= 1 sẽ có thể lấy số không phải tự nhiên như 1.5
    n = int(input("Đây không phải hệ phương trình, vui lòng nhập lại: "))
# Khởi tạo ma trận hệ số A và vector kết quả B
A = np.zeros((n, n))
B = np.zeros(n)

# Nhập ma trận hệ số A
print("Nhập ma trận hệ số A:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

# Nhập vector kết quả B
print("Nhập vector kết quả B:")
for i in range(n):
    B[i] = float(input(f"B[{i+1}]: "))

try:
    # Kiểm tra trường hợp ma trận A và vector kết quả B đều toàn số 0
    # toàn bộ các giá trị đã nhập
    if np.all(A == 0) and np.all(B == 0):
        print("Hệ phương trình vô số nghiệm.")
    else:
        # Tính bậc thang của ma trận A
        rref_A, _ = np.linalg.qr(A)

        # Số cột (hoặc hàng) độc lập tương ứng với bậc thang
        
        num_independent_columns = np.sum(np.abs(np.diag(rref_A)) > 1e-10)

        # Số biến tự do
        # phụ thuộc vào các thuộc tính của ma trận
        num_free_variables = A.shape[1] - num_independent_columns

        # Kiểm tra và in kết quả
        if num_free_variables > 0:
            print("Hệ phương trình có vô số nghiệm.")
        elif num_free_variables == 0:
            X = np.linalg.solve(A, B)
            print("Nghiệm của hệ phương trình:")
            for i in range(n):
                print(f"x[{i + 1}] = {X[i]}")
except np.linalg.LinAlgError:
    print("Hệ phương trình vô nghiệm...")
