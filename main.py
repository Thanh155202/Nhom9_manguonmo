import tkinter as tk
from tkinter import messagebox
import numpy as np

def tao_mang():
    global arr, element_entries
    try:
        n = int(num_elements_entry.get())
        if n <= 0:
            messagebox.showerror("Lỗi", "Số phần tử phải là một số nguyên dương.")
            return

        arr = []
        element_entries = []  # Danh sách các ô nhập liệu cho phần tử của mảng
        for i in range(n):
            element_label = tk.Label(root, text=f"Phần tử {i + 1}:")
            element_label.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(root, width=10)
            entry.grid(row=i+2, column=1, padx=10, pady=5)
            element_entries.append(entry)

        # Tạo các nút sau khi đã nhập số phần tử
        tao_nut()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên dương cho số phần tử.")

def tao_nut():
    global tang_dan, giam_dan, max, min, ket_qua

    # Nút để sắp xếp tăng dần
    tang_dan = tk.Button(root, text="Sắp xếp Tăng Dần", command=ham_tang_dan)
    tang_dan.grid(row=len(element_entries) + 3, column=0, columnspan=2, pady=10)

    # Nút để sắp xếp giảm dần
    giam_dan = tk.Button(root, text="Sắp xếp Giảm Dần", command=ham_giam_dan)
    giam_dan.grid(row=len(element_entries) + 4, column=0, columnspan=2, pady=5)

    # Nút để tìm giá trị lớn nhất
    max = tk.Button(root, text="Tìm Giá Trị Lớn Nhất", command=max_value)
    max.grid(row=len(element_entries) + 5, column=0, columnspan=2, pady=5)

    # Nút để tìm giá trị nhỏ nhất
    min = tk.Button(root, text="Tìm Giá Trị Nhỏ Nhất", command=min_value)
    min.grid(row=len(element_entries) + 6, column=0, columnspan=2, pady=5)

    # Label để hiển thị kết quả
    ket_qua = tk.Label(root, text="", wraplength=400)
    ket_qua.grid(row=len(element_entries) + 7, column=0, columnspan=2, pady=10)

def ham_tang_dan():
    if 'arr' in globals():
        try:
            arr = [int(entry.get()) for entry in element_entries]
            unique_arr = np.unique(arr)  # Loại bỏ các phần tử trùng lặp
            sorted_arr = np.sort(unique_arr)
            ket_qua.config(text="Mảng đã sắp xếp tăng dần: " + ", ".join(map(str, sorted_arr)))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập các phần tử của mảng là số nguyên.")
    else:
        messagebox.showerror("Lỗi", "Vui lòng tạo mảng trước khi sắp xếp.")

def ham_giam_dan():
    if 'arr' in globals():
        try:
            arr = [int(entry.get()) for entry in element_entries]
            unique_arr = np.unique(arr)  # Loại bỏ các phần tử trùng lặp
            sorted_arr = np.sort(unique_arr)[::-1]
            ket_qua.config(text="Mảng đã sắp xếp giảm dần: " + ", ".join(map(str, sorted_arr)))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập các phần tử của mảng là số nguyên.")
    else:
        messagebox.showerror("Lỗi", "Vui lòng tạo mảng trước khi sắp xếp.")

def max_value():
    if 'arr' in globals():
        try:
            arr = [int(entry.get()) for entry in element_entries]
            unique_arr = np.unique(arr)  # Loại bỏ các phần tử trùng lặp
            max_val = np.max(unique_arr)
            ket_qua.config(text="Giá trị lớn nhất trong mảng: " + str(max_val))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập các phần tử của mảng là số nguyên.")
    else:
        messagebox.showerror("Lỗi", "Vui lòng tạo mảng trước khi tìm giá trị lớn nhất.")

def min_value():
    if 'arr' in globals():
        try:
            arr = [int(entry.get()) for entry in element_entries]
            unique_arr = np.unique(arr)  # Loại bỏ các phần tử trùng lặp
            min_val = np.min(unique_arr)
            ket_qua.config(text="Giá trị nhỏ nhất trong mảng: " + str(min_val))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập các phần tử của mảng là số nguyên.")
    else:
        messagebox.showerror("Lỗi", "Vui lòng tạo mảng trước khi tìm giá trị nhỏ nhất.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Ứng dụng Mảng")

# Tạo label và ô nhập số phần tử
num_elements_label = tk.Label(root, text="Nhập số phần tử của mảng:")
num_elements_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
num_elements_entry = tk.Entry(root, width=10)
num_elements_entry.grid(row=0, column=1, padx=10, pady=5)

# Nút để tạo mảng
create_array_button = tk.Button(root, text="Tạo Mảng", command=tao_mang)
create_array_button.grid(row=1, column=0, columnspan=2, pady=10)

# Khởi chạy giao diện
root.mainloop()
