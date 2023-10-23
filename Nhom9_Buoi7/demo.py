import cv2
import os
import hashlib
from datetime import datetime
import tkinter as tk


# Tạo giao diện GUI
root = tk.Tk()
root.title("Ứng dụng nhận diện khuôn mặt")
root.geometry("800x450")  # Set the initial window size

# Thêm hình nền
hinh_nền = tk.PhotoImage(file="b.png")
background_label = tk.Label(root, image=hinh_nền)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Thực hiện các chức năng
def nhandang():
    def nhandang_luu():
        # Tạo thư mục lưu
        output_folder = 'faces'
        os.makedirs(output_folder, exist_ok=True)

        # tạo danh sách trống
        ds_trong = []

        # Tạo đối tượng Cascade Classifier bằng tệp XML Haar Cascade để nhận diện khuôn mặt
        face_cascade = cv2.CascadeClassifier('nhandien.xml')

        # mở camera
        cap = cv2.VideoCapture(0)

        # Sử dụng một biến để theo dõi xem từng khuôn mặt đã được lưu hay chưa
        face_saved = False

        while True:
            # đọc video từ camera
            ret, frame = cap.read()

            if not ret:
                break

            # Chuyển đổi hình ảnh sang thang độ xám để xử lý dễ dàng
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # sử dụng  Cascade Classifier để nhận diện khuôn mặt
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Lưu hình ảnh khuôn mặt không trùng lặp với tên chứa dấu thời gian
            if not face_saved and len(faces) > 0:
                for i, (x, y, w, h) in enumerate(faces):
                    face_image = frame[y:y + h, x:x + w]

                    # Tính giá trị hash của hình ảnh khuôn mặt để kiểm tra sự trùng lặp
                    hash_value = hashlib.md5(face_image.tobytes()).hexdigest()

                    # kiem tra nếu khuôn mặt chưa xh trong list
                    if hash_value not in ds_trong:
                        ds_trong.append(hash_value)

                        #Lấy thời gian thuc
                        current_time = datetime.now()
                        current_time_str = current_time.strftime('%Y%m%d%H%M%S')

                        # Tạo tên tệp bằng cách kết hợp dấu thời gian và chỉ mục
                        image_filename = os.path.join(output_folder, f'face_{current_time_str}_{i}.jpg')
                        cv2.imwrite(image_filename, face_image)

                        face_saved = True  # Đánh dấu ảnh đã được lưu cho khuôn mặt hiện tại

            # Vẽ hình chữ nhật xung quanh các khuôn mặt được phát hiện và hiển thị số lượng khuôn mặt được phát hiện
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # hiển thị số khuôn mặt được phát hiện
            face_count = len(faces)
            cv2.putText(frame, f'So khuon mat duoc phat hien: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # video ra
            cv2.imshow('FACE DETECTION', frame)

            # Đặt biến `face_saved` về Sai để cho phép lưu ảnh cho khuôn mặt tiếp theo
            if face_saved and len(faces) == 0:
                face_saved = False

            # thoát chương trình
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Giải phóng tài nguyên
        cap.release()
        cv2.destroyAllWindows()

    # Bắt đầu quá trình nhận diện khuôn mặt trong một qt  mới
    import threading
    threading.Thread(target=nhandang_luu).start()

# Mở folder chứa gương mặt được nhận dạng
def mo_tmuc():
    folder_path = os.path.abspath('faces')
    os.system(f'explorer {folder_path}')  

# Thoát chương trình
def thoat():
    root.destroy()

# tạo tiêu đề
title_label = tk.Label(root, text="ỨND DỤNG NHẬN DIỆN KHUÔN MẶT", font=("Comic Sans MS", 25))
title_label.grid(row=0, column=0, columnspan=3, pady=20)  # Place the title label in a single row

# tạo
start_button = tk.Button(root, text="Bắt đầu nhận diện", command=nhandang,bg="green",fg="white",font=("Comic Sans MS", 20))
open_folder_button = tk.Button(root, text="Mở thư mục ảnh", command=mo_tmuc,bg="lavender", font=("Comic Sans MS", 20))
exit_button = tk.Button(root, text="Thoát chương trình", command=thoat,bg="red",fg="white", font=("Comic Sans MS", 20))

start_button.grid(row=1, column=0, pady=20, padx=10)
open_folder_button.grid(row=1, column=1, pady=20, padx=10)
exit_button.grid(row=1, column=2, pady=20, padx=10)

# thoát chương trình
root.bind('q', thoat)

root.mainloop()
