import sys
from PyQt5.QtWidgets import *
import pyautogui
import time
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('C8763')
        self.initUI()

    def initUI(self):
        SWidth, SHeight = pyautogui.size()
        WWidth, WHeight = SWidth//3, SHeight//2
        x = (SWidth-WWidth)//2
        y = (SHeight-WHeight)//2
        self.setGeometry(x, y, WWidth, WHeight)

        self.vbox = QWidget(self)
        self.vbox.setGeometry(0,0,WWidth,WHeight//3)
        v_layout = QVBoxLayout(self.vbox)
        h_layout = QHBoxLayout(self.vbox)

        self.btn1 = QPushButton('myYouTube')
        self.btn1.setStyleSheet("font-size: 30px; font-family: Arial; color: red;")
        self.btn1.setFlat(True) #按鈕的背景邊框透明

        self.searchBox = QLineEdit(self)
        self.searchBox.resize(150, 25)

        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.searchBox)

        h_layout.addStretch(1)  # 在左側添加伸展彈簧，將物件推到右側
        h_layout.addLayout(v_layout)
        h_layout.addStretch(1)  # 在右側添加伸展彈簧，將物件推到左側
        

        
        v_layout.addLayout(h_layout)

        # v_layout.addWidget()


        # v_layout.addStretch(3)

        # self.btn1.clicked.connect(self.Btn1Click)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())