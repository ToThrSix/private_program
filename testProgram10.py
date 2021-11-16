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
        lbl_green.setStyleSheet("color:green;"
                                "background-color:#7FFFD4;")
        lbl_blue.setStyleSheet("color:blue;"
                                "background-color:#87CEFA;"
                                "border-style:dashed;"
                                "border-width:3px;"
                                "border-color:#1E90FF;")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle("Label Test")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram10()

    # python 2.7 기준으로는 exec()와 exec_()가 서로 다른 함수였지만
    # python 3.x 기준으로는 같은 함수이다.
    sys.exit(app.exec_())

        
