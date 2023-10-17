import cv2
import tkinter as tk
from tkinter import filedialog

def apply_edge_detection():
    lower_threshold = int(lower_threshold_entry.get())
    upper_threshold = int(upper_threshold_entry.get())
    # if image is not None:
    cv2.imshow("Ảnh ban đầu", image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)
    cv2.imshow("Ảnh sau khi tách biên", canny_image)

def open_image():
    global image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.ppm *.pgm")])
    if image_path:
        image = cv2.imread(image_path)
        if image is None:
            status_label.config(text="Không thể đọc ảnh. Vui lòng kiểm tra lại đường dẫn.")
        else:
            status_label.config(text="Ảnh đã chọn: " + image_path)

root = tk.Tk()
root.title("Edge Detection Application")

image = None

file_button = tk.Button(root, text="Chọn ảnh", command=open_image)
file_button.pack(pady=10)

lower_threshold_label = tk.Label(root, text="Ngưỡng dưới:")
lower_threshold_label.pack()
lower_threshold_entry = tk.Entry(root)
lower_threshold_entry.pack()

upper_threshold_label = tk.Label(root, text="Ngưỡng trên:")
upper_threshold_label.pack()
upper_threshold_entry = tk.Entry(root)
upper_threshold_entry.pack()

apply_button = tk.Button(root, text="Áp dụng tách biên", command=apply_edge_detection)
apply_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

root.mainloop()