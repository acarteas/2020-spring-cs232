import sys
import requests
from PySide2.QtUiTools import QUiLoader  # allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import QFile, QObject


class MainWindow(QObject):

    # class constructor
    def __init__(self, ui_file, parent=None):

        # call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        self._login_route = "http://localhost:5000/login"

        # load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        # always remember to close files
        ui_file.close()

        loginButton = self.window.findChild(QPushButton, 'loginButton')
        loginButton.clicked.connect(self.login)
        loginButton = self.window.findChild(QPushButton, 'cancelButton')
        loginButton.clicked.connect(self.close)

        # show window to user
        self.window.show()

    def close(self):
        self.window.close()

    def login(self):
        user_name = self.window.findChild(QLineEdit, 'userNameLineEdit').text()
        password = self.window.findChild(QLineEdit, 'passwordLineEdit').text()
        payload = {'user_name': user_name, 'password': password}
        result = requests.post(url=self._login_route, data=payload)

        message = QMessageBox()
        if result.text == "success":
            message.setText("Login successful.")
        else:
            message.setText("Bad user name or password.")
        message.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('LoginWindow.ui')
    sys.exit(app.exec_())
