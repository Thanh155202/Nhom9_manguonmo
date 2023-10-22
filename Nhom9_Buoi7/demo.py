import cv2
import os
import hashlib
from datetime import datetime

# Tạo một thư mục để lưu ảnh khuôn mặt
output_folder = 'faces'
os.makedirs(output_folder, exist_ok=True)

# Tạo một danh sách để lưu hash của khuôn mặt đã phát hiện
detected_faces_hash = []

# Tạo một đối tượng Cascade Classifier với tệp xml của Haar Cascade cho khuôn mặt
face_cascade = cv2.CascadeClassifier('nhan_dien.xml')

# Bật máy ảnh (thường là máy ảnh được tích hợp sẵn trên máy tính)
cap = cv2.VideoCapture(0)

# Sử dụng biến để theo dõi xem mỗi khuôn mặt đã được lưu hay chưa
face_saved = False

while True:
    # Đọc video từ máy ảnh
    ret, frame = cap.read()

    if not ret:
        break

    # Chuyển hình ảnh sang màu xám để dễ dàng xử lý
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Sử dụng Cascade Classifier để xác định khuôn mặt trong hình ảnh
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Lưu ảnh khuôn mặt không trùng lặp với tên bao gồm thời gian hiện tại
    if not face_saved and len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
            face_image = frame[y:y + h, x:x + w]

            # Tính hash của ảnh khuôn mặt để kiểm tra trùng lặp
            hash_value = hashlib.md5(face_image.tobytes()).hexdigest()

            # Kiểm tra xem khuôn mặt đã tồn tại trong danh sách hay chưa
            if hash_value not in detected_faces_hash:
                detected_faces_hash.append(hash_value)  # Thêm hash vào danh sách

                # Lấy thời gian hiện tại
                current_time = datetime.now()
                current_time_str = current_time.strftime('%Y%m%d%H%M%S')  # Định dạng ngày tháng giờ phút giây

                # Tạo tên tệp bằng cách kết hợp thời gian và số thứ tự
                image_filename = os.path.join(output_folder, f'face_{current_time_str}_{i}.jpg')
                cv2.imwrite(image_filename, face_image)

                face_saved = True  # Đánh dấu rằng đã lưu ảnh cho khuôn mặt hiện tại

    # Vẽ khung xung quanh khuôn mặt và hiển thị số lượng khuôn mặt đã phát hiện
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    # Hiển thị số khuôn mặt được phát hiện
    face_count = len(faces)
    cv2.putText(frame, f'So khuon mat : {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Hiển thị video đầu ra
    cv2.imshow('Nhận diện khuon mat', frame)

    # Đặt biến `face_saved` lại thành False để cho phép lưu ảnh cho khuôn mặt tiếp theo
    if face_saved and len(faces) == 0:
        face_saved = False

    # Thoát khỏi vòng lặp khi người dùng nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
