import sympy as sym
import tkinter as tk
from tkinter import ttk

def Xoa_dulieu():
    # Xóa dữ liệu
    for entry in entry_fields:
        entry.delete(0, 'end')
    for label in result_labels:
        label.config(text="")

def tichphan():
    bieuthuc  = bieuthuc_entry.get()
    bien = bien_entry.get()
    gh_tren = float(gh_tren_entry.get())
    gh_duoi = float(gh_duoi_entry.get())

    x = sym.symbols(bien)
    try:
        result = sym.integrate(bieuthuc, (x, gh_tren, gh_duoi))
        kq_tichphan.config(text="Result: " + str(result))
    except Exception as e:
        kq_tichphan.config(text="Error: " + str(e))

def gioihan():
    bieuthuc = gioihan_bieuthuc_entry.get()
    bien = gioihan_bien_entry.get()
    diem_gh = float(diem_gh_entry.get())

    x = sym.symbols(bien)
    try:
        result = sym.limit(bieuthuc, x, diem_gh)
        kq_gioihan.config(text="Gioi han at {}: {}".format(diem_gh, result))
    except Exception as e:
        kq_gioihan.config(text="Error: " + str(e))

def daoham():
    bieuthuc = daoham_bieuthuc_entry.get()
    bien = daoham_bien_entry.get()

    x = sym.symbols(bien)
    try:
        result = sym.diff(bieuthuc, x)
        daoham_result_label.config(text="daoham: " + str(result))
    except Exception as e:
        daoham_result_label.config(text="Error: " + str(e))

# tạo giao diện tkinder
root = tk.Tk()
root.title("ỨNG DỤNG MÔN GIẢI TÍCH")

# tạo các tab
tab_control = ttk.Notebook(root)
tichphan_tab = ttk.Frame(tab_control)
gioihan_tab = ttk.Frame(tab_control)
daoham_tab = ttk.Frame(tab_control)

tab_control.add(tichphan_tab, text="Tích Phân")
tab_control.add(gioihan_tab, text="Giới Hạn")
tab_control.add(daoham_tab, text="Đạo hàm")
tab_control.pack(expand=1, fill="both")

# tichphan tab
bieuthuc_label = ttk.Label(tichphan_tab, text="Nhập Biểu Thức:")
bieuthuc_label.grid(row=0, column=0)
bieuthuc_entry = ttk.Entry(tichphan_tab)
bieuthuc_entry.grid(row=0, column=1)

bien_label = ttk.Label(tichphan_tab, text="Biến:")
bien_label.grid(row=1, column=0)
bien_entry = ttk.Entry(tichphan_tab)
bien_entry.grid(row=1, column=1)

gh_tren_label = ttk.Label(tichphan_tab, text="Giới Hạn dưới:")
gh_tren_label.grid(row=2, column=0)
gh_tren_entry = ttk.Entry(tichphan_tab)
gh_tren_entry.grid(row=2, column=1)

gh_duoi_label = ttk.Label(tichphan_tab, text="Giới hạn trên:")
gh_duoi_label.grid(row=3, column=0)
gh_duoi_entry = ttk.Entry(tichphan_tab)
gh_duoi_entry.grid(row=3, column=1)

tichphan_button = ttk.Button(tichphan_tab, text="Tính Tích Phân", command=tichphan)
tichphan_button.grid(row=4, columnspan=2)

kq_tichphan = ttk.Label(tichphan_tab, text="")
kq_tichphan.grid(row=5, columnspan=2)

# gioihan tab
gioihan_bieuthuc_label = ttk.Label(gioihan_tab, text="Nhập biểu thức :")
gioihan_bieuthuc_label.grid(row=0, column=0)
gioihan_bieuthuc_entry = ttk.Entry(gioihan_tab)
gioihan_bieuthuc_entry.grid(row=0, column=1)

gioihan_bien_label = ttk.Label(gioihan_tab, text="Biến:")
gioihan_bien_label.grid(row=1, column=0)
gioihan_bien_entry = ttk.Entry(gioihan_tab)
gioihan_bien_entry.grid(row=1, column=1)

diem_gh_label = ttk.Label(gioihan_tab, text="Điểm Giới Hạn:")
diem_gh_label.grid(row=2, column=0)
diem_gh_entry = ttk.Entry(gioihan_tab)
diem_gh_entry.grid(row=2, column=1)

gioihan_button = ttk.Button(gioihan_tab, text="Tính Giới hạn", command=gioihan)
gioihan_button.grid(row=3, columnspan=2)

kq_gioihan = ttk.Label(gioihan_tab, text="")
kq_gioihan.grid(row=4, columnspan=2)


