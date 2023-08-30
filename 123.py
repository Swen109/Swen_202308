import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centered Widget Example')
        layout = QVBoxLayout()

        label = QLabel('Centered Widget', self)

        h_layout = QHBoxLayout()
        h_layout.addStretch(1)  # 在左側添加伸展彈簧，將物件推到右側
        h_layout.addWidget(label)
        h_layout.addStretch(1)  # 在右側添加伸展彈簧，將物件推到左側

        v_layout = QVBoxLayout()
        v_layout.addStretch(1)  # 在上方添加伸展彈簧，將物件推到下方
        v_layout.addLayout(h_layout)
        v_layout.addStretch(1)  # 在下方添加伸展彈簧，將物件推到上方

        layout.addLayout(v_layout)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
