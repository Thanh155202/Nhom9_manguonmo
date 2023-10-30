import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
def process_image():
    # Load the image
    file_path = filedialog.askopenfilename()
    image = cv2.imread(file_path)

    # Image processing steps (same as your code)
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    contrast_stretched_image = cv2.normalize(denoised_image, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    sharpened_image = cv2.filter2D(contrast_stretched_image, -1, kernel=kernel)
    brightness_image = cv2.convertScaleAbs(sharpened_image, alpha=1, beta=float(_beta.get()))
    gamma = float(_gamma.get())
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    gamma_corrected_image = cv2.LUT(brightness_image, lookup_table)

# Nhãn và thanh trượt cho tỉ lệ x
_beta = tk.Label(root, text="Độ mịn:")
_beta.pack()
_beta = tk.Scale(root, from_=0, to=50, resolution=1, orient="horizontal")
_beta.pack()

process_button = tk.Button(root, text='Chọn ảnh', command=process_image)
process_button.pack()

root.mainloop()
