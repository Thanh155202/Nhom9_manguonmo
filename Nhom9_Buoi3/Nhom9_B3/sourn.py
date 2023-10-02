import tkinter as tk
from tkinter import messagebox
import numpy as np


def create_matrix():
    global matrix_size
    matrix_size = int(entry_matrix_size.get())

    # Xóa cửa sổ chọn kích thước và hiển thị cửa sổ nhập giá trị ma trận
    size_window.destroy()
    create_matrix_input()


def create_matrix_input():
    global entry_values, matrix_frame

    matrix_frame = tk.Frame(root)
    matrix_frame.grid(row=0, column=0, padx=10, pady=10)

    entry_values = []

    for i in range(matrix_size):
        for j in range(matrix_size):
            label = tk.Label(matrix_frame, text=f"Nhập số tại hàng {i + 1}, cột {j + 1}:")
            label.grid(row=i, column=j * 2, padx=5, pady=5)
            entry_value = tk.Entry(matrix_frame)
            entry_value.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
            entry_values.append(entry_value)

    calculate_button = tk.Button(root, text="Tính toán", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)


def calculate():
    matrix = []
    for entry in entry_values:
        try:
            value = int(entry.get())
            matrix.append(value)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên.")
            return

    newarr = np.array(matrix).reshape(matrix_size, matrix_size)
    x = newarr.T  # Ma trận chuyển vị

    result_text.set(f"Ma trận đã nhập:\n{newarr}\n\nMa trận sau khi chuyển đổi:\n{x}")

    # Tính tích hai ma trận
    matrix_product = np.dot(newarr, x)
    result_text.set(result_text.get() + f"\n\nTích hai ma trận:\n{matrix_product}")


root = tk.Tk()
root.title("Chuyển đổi và tính tích ma trận")

matrix_size = 0
entry_values = []
matrix_frame = None

# Tạo cửa sổ chọn kích thước ma trận
size_window = tk.Toplevel(root)
size_window.title("Chọn kích thước ma trận")
size_label = tk.Label(size_window, text="Nhập kích thước ma trận (số hàng và số cột):")
size_label.pack()
entry_matrix_size = tk.Entry(size_window)
entry_matrix_size.pack()
create_matrix_button = tk.Button(size_window, text="Tạo ma trận", command=create_matrix)
create_matrix_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
