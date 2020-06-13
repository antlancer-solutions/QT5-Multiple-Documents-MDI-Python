from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
from PyQt5 import uic
import sys

class MDIWindow(QMainWindow):
    count = 0
    def __init__(self):

        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.menu_File.triggered[QAction].connect(self.WindowTrig)
        #self.setWindowTitle("MDI Application")

    def WindowTrig(self, p):
        if p.text() == "&New":
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("Sub Window" + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if p.text() == "&Cascade":
            self.mdi.cascadeSubWindows()
        if p.text() == "&Tile":
            self.mdi.tileSubWindows()
        #print (p.text())

app = QApplication(sys.argv)
mdi = MDIWindow()
mdi.show()
app.exec_()
