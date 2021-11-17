# Time Stamp

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime
from PyQt5.QtGui import QIcon

# # 년 월 일 요일
# now = QDate.currentDate()
# print(now.toString("d.M.yy"))
# print(now.toString("dd.MM.yyyy"))
# print(now.toString("ddd.MMMM.yyyy"))
# print(now.toString(Qt.ISODate))
# print(now.toString(Qt.DefaultLocaleLongDate))

# # 시 분 초 밀리초
# time = QTime.currentTime()
# print(time.toString("h.m.s"))
# print(time.toString("hh.mm.ss"))
# print(time.toString("hh.mm.ss.zzz"))
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))

# # 날짜 시간
# datetime = QDateTime.currentDateTime()
# print(datetime.toString("d.M.yy hh:mm:ss"))
# print(datetime.toString("dd.MM.yyyy. hh:mm:ss"))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))


class testProgram9(QMainWindow):

    def __init__(self):

        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon("../Image/exit.png"), "Exit", self)
        exitAction.setShortcut("ctrl+q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.toolBar = self.addToolBar("toolbar")
        self.toolBar.addAction(exitAction)

        self.setWindowTitle("show Date")
        self.setGeometry(300, 300, 500, 400)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram9()
    sys.exit(app.exec_())

