import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def select_image():
    global img, current_scale_x, current_scale_y
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        current_scale_x = 1.0
        current_scale_y = 1.0

# Hàm để thay đổi kích thước ảnh
def zoom_image():

    # Nhập tỉ lệ x và y từ người dùng qua giao diện Tkinter
    fx = float(scale_x.get())
    fy = float(scale_y.get())

    # Thay đổi kích thước ảnh theo tỉ lệ x và y
    resized_img = cv2.resize(img, (0, 0), fx=fx, fy=fy)

    # Hiển thị ảnh đầu ra sau khi zoom
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Ảnh ban đầu")
    plt.imshow(img, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title(f"Ảnh đã zoom (x={fx}, y={fy})")
    plt.imshow(resized_img, cmap='gray')
    plt.show()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Zoom Image")

# Tạo nút "Chọn ảnh" và đặt sự kiện khi nút này được nhấn
select_button = tk.Button(root, text="Chọn ảnh", command=select_image)
select_button.pack()

# Nhãn và thanh trượt cho tỉ lệ x và y
scale_x = tk.Label(root, text="Chiều x:")
scale_x.pack()
scale_x = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
scale_x.pack()
scale_y = tk.Label(root, text="Chiều y:")
scale_y.pack()
scale_y = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
scale_y.pack()

# Nút để thực hiện zoom ảnh
zoom_button = tk.Button(root, text="Zoom", command=zoom_image)
zoom_button.pack()

root.mainloop()
