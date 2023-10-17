import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Hàm để cập nhật và hiển thị ảnh sau khi zoom và quay ảnh
def update_image():
    rotated_img = cv2.warpAffine(original_img, cv2.getRotationMatrix2D((original_img.shape[1] / 2, original_img.shape[0] / 2), current_rotation, 1), (original_img.shape[1], original_img.shape[0]))
    scaled_img = cv2.resize(rotated_img, None, fx=current_scale, fy=current_scale, interpolation=cv2.INTER_LINEAR)
    img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def select_image():
    global original_img, current_scale, current_rotation
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        current_scale = 1.0
        current_rotation = 0
        update_image()
# Hàm xử lý sự kiện khi nút "Xác nhận Góc Quay" được nhấn
def change_rotation():
    global current_rotation
    rotation_text = rotation_entry.get()
    try:
        current_rotation = float(rotation_text)
        update_image()
    except ValueError:
        pass

# Tạo cửa sổ
window = tk.Tk()
window.title("Xoay ảnh")

# Khai báo biến toàn cục
current_scale = 1.0
current_rotation = 0
original_img = None
scale_factor = 1.2

# Tạo nút "Chọn ảnh" và đặt sự kiện khi nút này được nhấn
select_button = tk.Button(window, text="Chọn ảnh", command=select_image)
select_button.pack()


# Tạo hộp văn bản để nhập góc quay
rotation_label = tk.Label(window, text="Nhập góc quay (độ):")
rotation_label.pack()
rotation_entry = tk.Scale(window, from_=0, to=360, orient="horizontal")
rotation_entry.pack()
rotation_confirm_button = tk.Button(window, text="Xác nhận Góc Quay", command=change_rotation)
rotation_confirm_button.pack()


# Tạo label để hiển thị ảnh
img_label = tk.Label(window)
img_label.pack()

window.mainloop()
