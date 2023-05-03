from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
a = QApplication([])
w = QWidget()
w.setWindowTitle('gheg')
w.resize(300,300)
w.show()
l = QVBoxLayout()
b = QPushButton('gheg')
l.addWidget(b, alignment = Qt.AlignCenter)
w.setLayout(l)
def gheg():
    t = QLabel('gheg')
    l.addWidget(t, alignment = Qt.AlignCenter)
    w.setLayout(l)
b.clicked.connect(gheg)
a.exec_()