import sympy as sym
import tkinter as tk
from tkinter import ttk

# Xóa dữ liệu
def Xoa_dulieu():
    for entry in entry_fields:
        entry.delete(0, 'end')
    for label in result_labels:
        label.config(text="")

# Hàm tính tích phân
def tichphan():
    bieuthuc  = bieuthuc_entry.get()
    bien = bien_entry.get()
    gh_tren = float(gh_tren_entry.get())
    gh_duoi = float(gh_duoi_entry.get())

    x = sym.symbols(bien)
    try:
        result = sym.integrate(bieuthuc, (x, gh_tren, gh_duoi))
        kq_tichphan.config(text="Kết quả: " + str(result))
    except Exception as e:
        kq_tichphan.config(text="Lỗi: " + str(e))

