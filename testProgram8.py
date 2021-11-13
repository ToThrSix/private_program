# Set Position Center

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon

class testProgram8(QMainWindow):


    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon("exit.png"), "Exit", self)
        exitAction.setShortcut("ctrl+q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolBar = self.addToolBar("toolbar")
        self.toolBar.addAction(exitAction)

        self.setWindowTitle("Position : Center")
        self.resize(500, 400)
        self.center()
        self.show()

    def center(self):

        # 창의 위치와 크기 정보
        qr = self.frameGeometry()

        # 모니터의 가운데 위치 정보
        cp = QDesktopWidget().availableGeometry().center()

        # 위의 정보를 가지고 가운데 표시되는 위치 지정
        qr.moveCenter(cp)

        # 창이 가운데 표시됨
        self.move(qr.topLeft())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram8()
    sys.exit(app.exec_())