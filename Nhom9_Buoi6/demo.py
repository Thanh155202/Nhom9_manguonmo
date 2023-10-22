import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

# Global variables for image manipulation
original_img = None
current_scale = 1.0
current_rotation = 0
image = None

# Create the main application window
root = tk.Tk()
root.title("Scientific Image Processing")

# Function to update and display the image
def update_image():
    global image
    if original_img is not None:
        rotated_img = cv2.warpAffine(original_img, cv2.getRotationMatrix2D((original_img.shape[1] / 2, original_img.shape[0] / 2), current_rotation, 1), (original_img.shape[1], original_img.shape[0])
        )
        scaled_img = cv2.resize(rotated_img, None, fx=current_scale, fy=current_scale, interpolation=cv2.INTER_LINEAR)
        img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

# Function to open an image
def open_image():
    global original_img, current_scale, current_rotation
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.ppm *.pgm")])
    if file_path:
        original_img = cv2.imread(file_path)
        current_scale = 1.0
        current_rotation = 0
        update_image()

# Function to apply edge detection
def apply_edge_detection():
    lower_threshold = int(lower_threshold_entry.get())
    upper_threshold = int(upper_threshold_entry.get())
    if original_img is not None:
        cv2.imshow("Original Image", original_img)
        gray_image = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)
        cv2.imshow("Edge-Detected Image", canny_image)

# Create a notebook to organize different tabs
notebook = ttk.Notebook(root)
notebook.pack()

# Tab 1: Image Processing
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Image Processing")

# Open Image Button
open_button = tk.Button(tab1, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Label and Scale for Rotation
rotation_label = tk.Label(tab1, text="Enter Rotation Angle (degrees):")
rotation_label.pack()
rotation_scale = tk.Scale(tab1, from_=0, to=360, orient="horizontal", command=lambda val: [update_rotation(float(val))])
rotation_scale.set(0)
rotation_scale.pack()

# Label and Scale for Scaling
scaling_label = tk.Label(tab1, text="Enter Scaling Factor:")
scaling_label.pack()
scaling_scale = tk.Scale(tab1, from_=0.1, to=2, resolution=0.1, orient="horizontal", command=lambda val: [update_scaling(float(val))])
scaling_scale.set(1.0)
scaling_scale.pack()

# Image Display
img_label = tk.Label(tab1)
img_label.pack()

# Tab 2: Edge Detection
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Edge Detection")

# Lower Threshold
lower_threshold_label = tk.Label(tab2, text="Lower Threshold:")
lower_threshold_label.pack()
lower_threshold_entry = tk.Entry(tab2)
lower_threshold_entry.insert(0, "50")
lower_threshold_entry.pack()

# Upper Threshold
upper_threshold_label = tk.Label(tab2, text="Upper Threshold:")
upper_threshold_label.pack()
upper_threshold_entry = tk.Entry(tab2)
upper_threshold_entry.insert(0, "150")
upper_threshold_entry.pack()

# Apply Edge Detection Button
edge_detection_button = tk.Button(tab2, text="Apply Edge Detection", command=apply_edge_detection)
edge_detection_button.pack(pady=10)

# Function to update the rotation angle
def update_rotation(val):
    global current_rotation
    current_rotation = float(val)
    update_image()

# Function to update the scaling factor
def update_scaling(val):
    global current_scale
    current_scale = float(val)
    update_image()

# Start the Tkinter main loop
root.mainloop()
