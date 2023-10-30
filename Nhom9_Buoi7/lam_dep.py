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
    brightness_image = cv2.convertScaleAbs(sharpened_image, alpha=1, beta=10)
    gamma = 0.5
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    gamma_corrected_image = cv2.LUT(brightness_image, lookup_table)

    # Display the original and enhanced images using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('ảnh gốc')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(gamma_corrected_image, cv2.COLOR_BGR2RGB))
    plt.title('ảnh đã chỉnh')

    plt.show()


# Create a simple Tkinter GUI
root = tk.Tk()
root.title('Chỉnh ảnh')
root.geometry('400x200')

process_button = tk.Button(root, text='Chọn ảnh', command=process_image)
process_button.pack()

root.mainloop()
