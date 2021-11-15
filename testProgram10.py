import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, QLabel, QVBoxLayout

class testProgram10(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        # 라벨 생성
        lbl_red = QLabel("Red")
        lbl_blue = QLabel("Blue")
        lbl_green = QLabel("Green")

        # css 지정
        lbl_red.setStyleSheet("color:red;"
                                "border-style:solid;"
                                "border-width:2px;"
                                "border-color:#FA8072;"
                                "border-radius:3px;")
        
