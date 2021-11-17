# Create Menu Bar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, qApp
from PyQt5.QtGui import QIcon

# class가 ()안의 객체를 상속받은 것으로 생각하면 이해가 쉽다(?)
class testProgram6(QMainWindow):

    def __init__(self):
        
        # QMainWindow의 속성을 받아오기 위한 설정이다.
        super().__init__()
        self.initUI()

    def initUI(self):

        # icon, label, 대상 지정
        exitAction = QAction(QIcon("../Image/exit.png"), "Exit", self)

        # shortcut 지정
        exitAction.setShortcut("Ctrl+Q")

        #상태바에 메세지 표시
        exitAction.setStatusTip("Exit Application")

        # 해당 동작 선택 시 반응
        exitAction.triggered.connect(qApp.quit)

        btn = QPushButton("Exit", self)
        btn.move(400, 350)
        btn.resize(30, 20)
        btn.setStatusTip("Exit Application")
        btn.clicked.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # & 표시가 있으면 alt + 해당 글자로 단축키 가능
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        self.setWindowTitle("Menu Bar")
        self.setGeometry(300, 300, 500, 400)

        # 이 python 파일을 실행시켰을 때, 화면에 프로그램이 나오는 이유
        self.show()

if __name__ == "__main__":

    # app을 생성한다.
    app = QApplication(sys.argv)

    # class 내에 self.show()가 있기 때문에 class를 생성하면서
    # 자동으로 화면에 프로그램이 나타나게 된다.
    # 따라서 이 과정을 생략하게 되면 화면에 아무것도 나오지 않는 것.
    ex = testProgram6()

    # app.exec_()는 app 이 무한 대기 상태에 있도록 하는 명령
    # app이 중단되면 app.exec_()는 0을 return 한다.
    # 따라서 sys.exit(0)은 무한루프를 벗어나고 python이 종료된다.
    sys.exit(app.exec_())