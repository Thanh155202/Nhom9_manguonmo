import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Đọc dữ liệu từ tệp Excel
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành các đặc trưng và nhãn
X = data.drop('Performance Index', axis=1)
y = data['Performance Index']

# Chuẩn hóa dữ liệu
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
