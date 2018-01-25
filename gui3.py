#-'''- coding: utf-8 -'''-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit("")
        self.editout = QLineEdit("")
        self.button = QPushButton("calculate")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.editout)
        self.setLayout(layout)

        self.button.clicked.connect(self.calculate)

    def calculate(self):
        if(int(self.edit.text()) % 2 == 0):
            self.editout.setText("gu")
        else:
            self.editout.setText("ki")



if __name__ == '__main__':
    # Qt Applicationを作成します
    app = QApplication(sys.argv)
    # formを作成して表示します
    form = Form()
    form.show()
    # Qtのメインループを開始します
    sys.exit(app.exec_())