# Box Layout

import sys
from PyQt5.QtWidgets import QApplication, qApp, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

# QHBoxLayout과 QVBoxLayout은 box layout을 만들기 위한 클래스이다.

class testProgram11(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK", self)
        cancelButton = QPushButton("CANCEL", self)

        okButton.resize(okButton.sizeHint())
        cancelButton.resize(cancelButton.sizeHint())

        hBox = QHBoxLayout()
        hBox.addStretch(5)
        hBox.addWidget(okButton)
        hBox.addWidget(cancelButton)
        hBox.addStretch(1)

        vBox = QVBoxLayout()
        vBox.addStretch(5)
        vBox.addLayout(hBox)
        vBox.addStretch(1)

        self.setLayout(vBox)

        self.setWindowTitle("Box Layout")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram11()
    sys.exit(app.exec_())