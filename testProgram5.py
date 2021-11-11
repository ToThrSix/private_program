# Appear Status Bar
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMainWindow
from PyQt5.QtGui import QFont, QIcon

class testProgram5(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage("Ready")

        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("exit the program")

        btn = QPushButton("Quit", self)
        btn.move(300, 250)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QApplication.instance().quit)

        self.setWindowTitle("use ToolTip Bar")
        self.setWindowIcon(QIcon("Web.png"))
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram5()
    sys.exit(app.exec_())
