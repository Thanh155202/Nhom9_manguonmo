import cv2
import os
import hashlib
from datetime import datetime
import tkinter as tk



root = tk.Tk()
root.title("Ứng dụng nhận dang khuôn mặt")
root.geometry("800x450")
hinhnen = tk.PhotoImage(file="b.png")

# tao tieu de
background_label = tk.Label(root, image=hinhnen)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# bat dau các chức năng
def batdaunhandien():
    def nhandien_luu():
        # tạo thư mục lưu ảnh nếu nó chưa có
        output_folder = 'faces'
        os.makedirs(output_folder, exist_ok=True)

        detected_faces_hash = []
        face_cascade = cv2.CascadeClassifier('nhandien.xml')

        cap = cv2.VideoCapture(0)
        face_saved = False

        while True:
            ret, frame = cap.read()

            if not ret:
                break
                
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if not face_saved and len(faces) > 0:
                for i, (x, y, w, h) in enumerate(faces):
                    face_image = frame[y:y + h, x:x + w]
                    hash_value = hashlib.md5(face_image.tobytes()).hexdigest()

                    if hash_value not in detected_faces_hash:
                        detected_faces_hash.append(hash_value) 

                        # Get the current time
                        current_time = datetime.now()
                        current_time_str = current_time.strftime('%Y%m%d%H%M%S')  

                        image_filename = os.path.join(output_folder, f'face_{current_time_str}_{i}.jpg')
                        cv2.imwrite(image_filename, face_image)

                        face_saved = True 

            #vẽ hình vuông
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            #đếm sô gương mặt xh
            face_count = len(faces)
            cv2.putText(frame, f'So khuon mat duoc phat hien: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('FACE DETECTION', frame)

            if face_saved and len(faces) == 0:
                face_saved = False

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # giải phóng
        cap.release()
        cv2.destroyAllWindows()
        
    import threading
    threading.Thread(target=nhandien_luu).start()

def mo_thumuc():
    folder_path = os.path.abspath('faces')
    os.system(f'explorer {folder_path}') 

def thoat():
    root.destroy()

title_label = tk.Label(root, text="ỨNG DỤNG NHẬN DẠNG KHUÔN MẶT", font=("Comic Sans MS", 25))
title_label.grid(row=0, column=0, columnspan=3, pady=20)  # Place the title label in a single row


start_button = tk.Button(root, text="Bắt đầu nhận dạng", command=batdaunhandien,bg="green",fg="white",font=("Comic Sans MS", 20))
open_folder_button = tk.Button(root, text="Mở thư mục ảnh", command=mo_thumuc,bg="lavender", font=("Comic Sans MS", 20))
exit_button = tk.Button(root, text="Thoát chương trình", command=thoat,bg="red",fg="white", font=("Comic Sans MS", 20))

start_button.grid(row=1, column=0, pady=20, padx=10)
open_folder_button.grid(row=1, column=1, pady=20, padx=10)
exit_button.grid(row=1, column=2, pady=20, padx=10)

root.bind('q', thoat)

root.mainloop()