import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Nhãn và thanh trượt cho tỉ lệ x
_beta = tk.Label(root, text="Độ mịn:")
_beta.pack()
_beta = tk.Scale(root, from_=0, to=50, resolution=1, orient="horizontal")
_beta.pack()

process_button = tk.Button(root, text='Chọn ảnh', command=process_image)
process_button.pack()

root.mainloop()
