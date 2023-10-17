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
