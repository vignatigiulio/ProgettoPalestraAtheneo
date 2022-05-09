from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from Gestione_posta_e_account.Cambio_password.Controller.Cambio_password_controller import metodi_cambio_password
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class change_password(object):
    Controller = metodi_cambio_password()
    username = ""
    objMetodi = GestioneOggetti()

    def impostaPassword(self):
        esito_operazione = self.Controller.impostaPassword(self.cmbTipo.currentText(), self.txtPassword_1.text(),
                                        self.txtPassword_2.text(), self.username)
        if esito_operazione == 0:
            self.objMetodi.show_popup_ok("Salvataggio password è andato a buon fine.")
            self.finestre.close()
        elif esito_operazione == -1:
            self.objMetodi.show_popup_exception("La password è troppo corta.")
        elif esito_operazione == -2:
            self.objMetodi.show_popup_exception("Le due password sono diverse.")
        elif esito_operazione == -3:
            self.objMetodi.show_popup_exception("Errore. Controllare che la tipologia di cliente indicata sia esatta.")

    def cancella(self):
        self.txtPassword_1.clear()
        self.txtPassword_2.clear()

    def mostraPassword(self):
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def nascondiPassword(self):
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, MainWindow, username):
        self.finestre = MainWindow
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblPassword_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword_1.setGeometry(QtCore.QRect(30, 60, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblPassword_1.setFont(font)
        self.lblPassword_1.setObjectName("lblpsw")
        self.lblPassword_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword_2.setGeometry(QtCore.QRect(30, 100, 201, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblPassword_2.setFont(font)
        self.lblPassword_2.setObjectName("lblpsw_2")
        self.txtPassword_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword_2.setGeometry(QtCore.QRect(240, 100, 211, 31))
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword_2.setObjectName("txtPassword_2")
        self.txtPassword_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword_1.setGeometry(QtCore.QRect(240, 60, 211, 31))
        self.txtPassword_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword_1.setObjectName("txtPassword")
        self.btnCancella = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancella.setGeometry(QtCore.QRect(270, 150, 75, 24))
        self.btnCancella.setObjectName("btnCancella")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(360, 150, 81, 24))
        self.btnSalva.setObjectName("btnSalva")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 150, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Resources/images/password.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnMostraPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnMostraPassword.setGeometry(QtCore.QRect(420, 110, 21, 16))
        self.btnMostraPassword.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./Resources/images/pngGUI_client/download.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMostraPassword.setIcon(icon)
        self.btnMostraPassword.setIconSize(QtCore.QSize(20, 20))
        self.btnMostraPassword.setObjectName("btnMostraPassword")
        self.lblCondizione = QtWidgets.QLabel(self.centralwidget)
        self.lblCondizione.setGeometry(QtCore.QRect(30, 150, 201, 61))
        self.lblCondizione.setWordWrap(True)
        self.lblCondizione.setObjectName("lblCondizione")
        self.cmbTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cmbTipo.setGeometry(QtCore.QRect(30, 20, 141, 28))
        self.cmbTipo.setObjectName("cmbTipo")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnSalva.clicked.connect(self.impostaPassword)
        self.btnCancella.clicked.connect(self.cancella)
        self.btnMostraPassword.pressed.connect(self.mostraPassword)
        self.btnMostraPassword.clicked.connect(self.nascondiPassword)
        self.txtPassword_1.setFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cambio password"))
        self.cmbTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.cmbTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Staff", None))
        self.lblPassword_1.setText(_translate("MainWindow", "Inserisci la nuova password:"))
        self.lblPassword_2.setText(_translate("MainWindow", "Conferma la nuova password:"))
        self.btnCancella.setText(_translate("MainWindow", "Cancell"))
        self.btnSalva.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = change_password()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())