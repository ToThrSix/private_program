# ToolBar

import sys

# QtWidgets.qApp은 QtWidgets.QApplication.instance() 와 
# 동일한 모습을 보이지만 QApplication이 생성되지 않으면 에러가 발생한다.
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class testProgram7(QMainWindow):

    # testProgram7의 생성자
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon("exit.png"), "Exit", self)

        #대소문자의 영향을 받지는 않는다.
        exitAction.setShortcut("Ctrl+q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon("save.png"), "Save", self)
        saveAction.setShortcut("ctrl+s")
        saveAction.setStatusTip("Save Configuration")

        # status bar 생성
        # 여기에 Status Tip 출력
        self.statusBar()

        # 하나의 ToolBar를 생성하는 명령
        self.toolBar = self.addToolBar("Exit")

        # 해당 툴바에 Action 추가
        self.toolBar.addAction(exitAction)
        self.toolBar.addAction(saveAction)

        self.setWindowTitle("use ToolBar")
        self.setGeometry(300, 300, 500, 400)
        self.show()


if __name__ == "__main__":

    #여기서 QApplication이 생섣되기 때문에
    # class 내에서 qApp으로 간편하게 사용 가능한 것
    app = QApplication(sys.argv)
    ex = testProgram7()
    sys.exit(app.exec_())
