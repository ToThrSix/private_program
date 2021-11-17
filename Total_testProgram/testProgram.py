# Practice to make a private program.
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class testProgram(QWidget):

    def __init__(self):
    
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
    
        self.setWindowTitle("This is my first program.")
        self.move(300, 300)
        self.resize(500, 400)
        self.show()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = testProgram()
    sys.exit(app.exec_())
