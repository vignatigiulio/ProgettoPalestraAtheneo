from PyQt5 import QtCore, QtWidgets
from Gestione_posta_e_account.Posta.View.Casella_risposta import casella_risposta



class lettura_messaggio(object):
    username = ""

    def apriCasellaMessaggi(self):
        self.casella_risposta = QtWidgets.QMainWindow()
        self.ui = casella_risposta()
        self.ui.setupUi(self.casella_risposta, self.objMessaggio)
        self.casella_risposta.show()

    def setupUi(self, MainWindow, oggetto_messaggio, username):
        self.objMessaggio = oggetto_messaggio
        self.username = username
        self.finestra = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ptxContenuto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxContenuto.setGeometry(QtCore.QRect(90, 110, 481, 241))
        self.ptxContenuto.setObjectName("ptxContenuto")
        self.ptxContenuto.setReadOnly(True)
        self.btnRispondi = QtWidgets.QPushButton(self.centralwidget)
        self.btnRispondi.setGeometry(QtCore.QRect(310, 370, 121, 28))
        self.btnRispondi.setObjectName("btnRispondi")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(450, 370, 121, 28))
        self.btnIndietro.setObjectName("btnIndietro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        if self.objMessaggio.mittente == self.username:
            self.btnRispondi.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnIndietro.clicked.connect(self.finestra.close)
        self.btnRispondi.clicked.connect(self.apriCasellaMessaggi)
        self.ptxContenuto.setPlainText(self.objMessaggio.contenuto)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Messaggio"))
        self.btnRispondi.setText(_translate("MainWindow", "Rispondi"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = lettura_messaggio()
    ui.setupUi(MainWindow, "", )
    MainWindow.show()
    sys.exit(app.exec_())
