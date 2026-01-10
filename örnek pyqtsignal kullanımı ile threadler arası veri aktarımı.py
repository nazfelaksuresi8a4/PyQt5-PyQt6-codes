from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import sys as _s 
import time as t

class ThreadSide(QObject):
    signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.run)

    def run(self,lst):
        print(lst)

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton(self,text='main')

        btn.clicked.connect(self.ignit)
    
    def ignit(self):
        self.threaD = ThreadSide()
        self.threaD.signal.emit([2,4,6,8,10,12])

if __name__=="__main__":
    sp = QApplication(_s.argv)
    sw = mainWindow()
    sw.show()
    _s.exit(sp.exec_())
