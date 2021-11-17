# Appear ToolTip
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

class testProgram4(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Quit", self)
        btn.move(300, 250)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("Appear ToolTip")
        self.setWindowIcon(QIcon("Web.png"))
        self.setGeometry(300,300,400,300)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram4()
    sys.exit(app.exec_())