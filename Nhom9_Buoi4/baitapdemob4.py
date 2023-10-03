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

#Hàm tính giới hạn
def gioihan():
    bieuthuc = gioihan_bieuthuc_entry.get()
    bien = gioihan_bien_entry.get()
    diem_gh = float(diem_gh_entry.get())

    x = sym.symbols(bien)
    try:
        result = sym.limit(bieuthuc, x, diem_gh)
        kq_gioihan.config(text="Giới hạn tại điểm {}: {}".format(diem_gh, result))
    except Exception as e:
        kq_gioihan.config(text="Lỗi: " + str(e))

# Hàm tính đạo hàm
def daoham():
    bieuthuc = daoham_bieuthuc_entry.get()
    bien = daoham_bien_entry.get()

    x = sym.symbols(bien)
    try:
        result = sym.diff(bieuthuc, x)
        daoham_result_label.config(text="Kết quả đạo hàm: " + str(result))
    except Exception as e:
        daoham_result_label.config(text="Error: " + str(e))

