from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import sys as _s 
import time as t

class ThreadSide(QObject):
    def __init__(self):
        super().__init__()
        self.signal = 0
    
    def run(self):
        for i in range(10):
            t.sleep(0.5)
            print(i)

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton(self,text='main')

        btn.clicked.connect(self.ignit)
    
    def ignit(self):
        self.threaD = ThreadSide()
        self.mainThread = QThread(self)
        self.threaD.moveToThread(self.mainThread)
        
        self.mainThread.started.connect(self.threaD.run)
        self.mainThread.start()

if __name__=="__main__":
    sp = QApplication(_s.argv)
    sw = mainWindow()
    sw.show()
    _s.exit(sp.exec_())
