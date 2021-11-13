# Create Menu Bar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, qApp
from PyQt5.QtGui import QIcon

class testProgram6(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon("exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")

        #상태바에 메세지 표시
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        btn = QPushButton("Exit", self)
        btn.move(400, 350)
        btn.resize(30, 20)
        btn.setStatusTip("Exit Application")
        btn.clicked.connect(QApplication.instance().quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        self.setWindowTitle("Menu Bar")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram6()
    sys.exit(app.exec_())