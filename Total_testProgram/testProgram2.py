# 2nd Test Program
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class testProgram2(QWidget):

    def __init__(self):
    
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Edit Window Title Icon")

        # 어떤 아이콘을 사용할 것인지 설정
        self.setWindowIcon(QIcon("../Image/web.png"))

        # setGeometry method는 move와 resize를 합쳐놓은 method이다.
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram2()
sys.exit(app.exec_())
