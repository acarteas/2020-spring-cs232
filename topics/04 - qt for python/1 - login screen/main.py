import sys
import os
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import QFile, QObject
import requests

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        #always remember to close files
        ui_file.close()

        login_button = self.window.findChild(QPushButton, 'loginButton')
        login_button.clicked.connect(self.login_clicked)

        cancel_button = self.window.findChild(QPushButton, 'cancelButton');
        cancel_button.clicked.connect(self.cancel_clicked)

        #show should be last
        self.window.show()

    def cancel_clicked(self):
        self.window.close()

    def login_clicked(self):
        #disable login button while we wait
        login_button = self.window.findChild(QPushButton, 'loginButton')
        login_button.setEnabled(False)
        self.window.statusBar().showMessage("Logging in...")

        user_name = self.window.findChild(QLineEdit, 'userNameLineEdit').text()
        password = self.window.findChild(QLineEdit, 'passwordLineEdit').text()

        url = 'http://localhost:5000/login'
        data = {'user_name' : user_name, 'password': password}

        #send to web server
        result = requests.post(url = url, data = data)
        message_box = QMessageBox()
        if result.text == "success":
            message_box.setText("You are now logged in!")
        else:
            message_box.setText("Invalid user name or password")
        message_box.exec()
        
        login_button.setEnabled(True)
        self.window.statusBar().showMessage("")

if __name__ == '__main__':

    #from SO: https://stackoverflow.com/questions/41331201/pyqt-5-and-4k-screen
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    main_window = MainWindow('login.ui')
    sys.exit(app.exec_())

