import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Đọc dữ liệu từ tệp Excel
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành các đặc trưng và nhãn
X = data.drop('Performance Index', axis=1)
y = data['Performance Index']


