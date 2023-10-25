import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QImage, QImageReader, QImageWriter, QImage.Format_RGB888
from PyQt5.QtCore import Qt

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
        self.img = cv2.imread('pic2.png')
        self.display_image(self.img)

    def initUI(self):
        self.setWindowTitle('Beauty Image Processing App')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.original_label = QLabel(self)
        self.layout.addWidget(self.original_label)

        self.sharpen_button = QPushButton('Sharpen', self)
        self.layout.addWidget(self.sharpen_button)
        self.sharpen_button.clicked.connect(self.apply_sharpen)

        self.excessive_sharpen_button = QPushButton('Excessive Sharpen', self)
        self.layout.addWidget(self.excessive_sharpen_button)
        self.excessive_sharpen_button.clicked.connect(self.apply_excessive_sharpen)

        self.edge_enhancement_button = QPushButton('Edge Enhancement', self)
        self.layout.addWidget(self.edge_enhancement_button)
        self.edge_enhancement_button.clicked.connect(self.apply_edge_enhancement)

    def display_image(self, image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        self.original_label.setPixmap(pixmap)
        self.original_label.setAlignment(Qt.AlignCenter)

    def apply_filter(self, kernel):
        output_image = cv2.filter2D(self.img, -1, kernel)
        self.display_image(output_image)

    def apply_sharpen(self):
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        self.apply_filter(kernel)

    def apply_excessive_sharpen(self):
        kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1])
        self.apply_filter(kernel)

    def apply_edge_enhancement(self):
        kernel = np.array([[-1, -1, -1, -1, -1],
                           [-1, 2, 2, 2, -1],
                           [-1, 2, 8, 2, -1],
                           [-1, 2, 2, 2, -1],
                           [-1, -1, -1, -1, -1]]) / 8.0
        self.apply_filter(kernel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessingApp()
    ex.show()
    sys.exit(app.exec_())
