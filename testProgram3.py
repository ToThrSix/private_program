# Use Button to close the program
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class testProgram3(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("use Button to close the widget")
        self.setGeometry(300, 300, 500, 400)
        self.setWindowIcon(QIcon("web.png"))
        
        btn = QPushButton("Quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram3()
    sys.exit(app.exec_())