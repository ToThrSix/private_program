# Grid Layout

import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon

class testProgram12(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        # Grid Layout을 설정하기 위한 객체 생성
        grid = QGridLayout()
        
        # 위젯에 레이아웃 설정
        self.setLayout(grid)

        grid.addWidget(QLabel("Title"), 0, 0)
        grid.addWidget(QLabel("Author"), 1, 0)
        grid.addWidget(QLabel("Review"), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        # 궁금증: 왜 grid layout은 setLayout을 먼저 했을까?
        # self.setLayout(grid)를 나중에 선언하면 어떻게 될까?

        # 화면을 띄우기 위한 기본적인 명령어
        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram12()
    sys.exit(app.exec_())