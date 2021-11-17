# Box Layout

import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

# QHBoxLayout과 QVBoxLayout은 box layout을 만들기 위한 클래스이다.

class testProgram11(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPuchButton("OK", self)
        cancelButton = QPushButton("CANCEL", self)

        okButton.resize(okButton.sizeHine())
        cancelButton.resize(calcelButton.sizeHine())

        vBox = QVBoxLayout()
        vBox.addStretch(5)
        vBox.addWidget(okButton)
        vBox.addWidget(cancelButton)
        vBox.addStretch(1)

        hBox = QHBoxLayout()
        hBox.addStretch(5)
        hBox.addLayout(vBox)
        hBox.addStretch(1)

        self.setLayout(hBox)

        self.setWindowTitle("Box Layout")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram11()
    sys.exit(app.exec_())