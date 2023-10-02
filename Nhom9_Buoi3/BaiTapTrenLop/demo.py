import tkinter as tk
from tkinter import END, Scrollbar, Text
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a custom color palette
custom_colors = ['#FF5733', '#33FF57', '#33AFFF', '#AFFF33', '#FF33AF', '#33FFAF', '#FF5733', '#AFAF33']

# Create a custom font
custom_font = ('Helvetica', 12)

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df)

def tongsinhvien():
    sv = in_data[:, 1]
    tongsv = np.sum(sv)
    result_text.insert(END, "Tổng số sinh viên đi thi: " + str(tongsv) + " sinh viên\n")

    svtruot = in_data[:, 10]
    tongsvtruot = np.sum(svtruot)
    tongsvdat = tongsv - tongsvtruot

    percent_dat = round((tongsvdat / tongsv) * 100, 2)
    percent_truot = round((tongsvtruot / tongsv) * 100, 2)

    result_text.insert(END, "Tổng số sinh viên qua môn: " + str(tongsvdat) + " sinh viên (" + str(percent_dat) + "%)\n")
    result_text.insert(END, "Tổng số sinh viên trượt môn: " + str(tongsvtruot) + " sinh viên (" + str(percent_truot) + "%)\n\n")
    categories = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']
    values1 = np.sum(in_data[0:9, 2:10], axis=1).flatten()
    values2 = in_data[:, 10]

    fig, ax1 = plt.subplots(figsize=(8, 18))

    ax1.bar(categories, values1, color='green', label="Sinh viên đạt")
    ax1.bar(categories, values2, bottom=values1, color='red', label="Sinh viên trượt")

    for i, (v1, v2) in enumerate(zip(values1, values2)):
        ax1.text(i, v1/2, str(v1), ha='center', va='bottom', color='white', fontweight='bold')
        ax1.text(i, v1 + v2/2, str(v2), ha='center', va='bottom', color='white', fontweight='bold')

    ax1.set_title('Biểu đồ số sinh viên đạt, trượt của từng lớp')
    ax1.set_ylabel('Số sinh viên')
    ax1.legend(loc='upper right')

    plt.subplots_adjust(hspace=0.5)
    plt.show()

def sinhvienA():
    diemA = in_data[:, 3]
    maxa = diemA.max()
    i = np.argmax(diemA)
    result_text.config(state=tk.NORMAL)
    result_text.insert(END, 'Lớp có nhiều sinh viên đạt điểm A nhất là lớp {0} có {1} sinh viên\n'.format(in_data[i, 0], maxa))

    categories1 = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']
    values1 = in_data[:, 3]

    plt.figure(4)
    bars = plt.bar(categories1, values1, label="Lớp có nhiều sinh viên điểm A nhất", color=custom_colors)
    plt.title('Biểu đồ số sinh viên đạt điểm A của các lớp')
    plt.ylabel('Số sinh viên')
    plt.legend(loc='upper right')

    for bar, value in zip(bars, values1):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, value, ha='center', va='bottom')

    plt.show()

def phodiem():
    labels = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    diems = in_data[:, 3:11]
    total_students = diems.shape[0]
    grade_counts = diems.sum(axis=0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Bar chart
    ax1.bar(labels, grade_counts, color=custom_colors)
    ax1.set_xlabel('Điểm')
    ax1.set_ylabel('Số lượng sinh viên')
    ax1.set_title('Phổ điểm')
    for i, v in enumerate(grade_counts):
        ax1.annotate(str(v), (i, v), ha='center', va='bottom')

    # Pie chart
    ax2.pie(grade_counts, labels=labels, autopct='%1.1f%%', colors=custom_colors)
    ax2.axis('equal')
    ax2.set_title('Phổ điểm')

    plt.tight_layout()
    plt.show()

def compare_l1_l2_chart():
    l1_counts = in_data[:, 11]
    l2_counts = in_data[:, 12]
    class_labels = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']

    plt.figure(figsize=(10, 6))
    plt.bar(class_labels, l1_counts, width=0.4, label='L1', color='blue')
    plt.bar(class_labels, l2_counts, width=0.4, label='L2', color='red', bottom=l1_counts)
    plt.xlabel('Lớp')
    plt.ylabel('Số lượng sinh viên')
    plt.title('So sánh điểm L1 và L2 cho mỗi lớp')
    plt.legend()
    plt.show()

def reset_result():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, END)
    plt.close('all')
    result_text.config(state=tk.DISABLED)

# Create a tkinter window
window = tk.Tk()
window.title("Bảng báo cáo kết quả thi")

# Create a centered title label
title_label = tk.Label(window, text="Bảng báo cáo kết quả thi", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Create buttons for the remaining functionalities with adjusted size and fonts
button_width = 15
button_font = ('Helvetica', 10)

tongsinhvien_button = tk.Button(window, text="Tổng số SV đi thi", command=tongsinhvien, width=button_width, font=button_font)
sinhvienA_button = tk.Button(window, text="Lớp có nhiều SV điểm A nhất", command=sinhvienA, width=button_width, font=button_font)
phodiem_button = tk.Button(window, text="Phổ điểm", command=phodiem, width=button_width, font=button_font)
compare_l1_l2_chart_button = tk.Button(window, text="So sánh điểm L1 và L2", command=compare_l1_l2_chart, width=button_width, font=button_font)

reset_button = tk.Button(window, text="Reset", command=reset_result, width=button_width, font=button_font)

# Create an output Text widget
result_text = Text(window, wrap="word", height=20, width=200)
result_text_scrollbar = Scrollbar(window, command=result_text.yview)
result_text.config(yscrollcommand=result_text_scrollbar.set)

# Arrange buttons in a 2x2 grid
tongsinhvien_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
sinhvienA_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
phodiem_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
compare_l1_l2_chart_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Place the result_text widget below the buttons
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Place the reset_button below the 2x2 grid
reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


# Main loop
window.mainloop()