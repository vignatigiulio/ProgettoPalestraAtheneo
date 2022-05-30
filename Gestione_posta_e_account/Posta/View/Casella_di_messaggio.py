from PyQt5 import QtCore, QtGui, QtWidgets
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from datetime import datetime
from Gestione_posta_e_account.Posta.Controller.Messaggio_controller import metodi_gestione_messaggi

class Casella_di_messaggio(object):

    objMetodi = GestioneOggetti()
    username = ""

    Controller = metodi_gestione_messaggi()

    def popola_comboBox(self):
        self.lblMittente.setText(self.username)
        if self.username != "Admin":
            self.cmbDestinatari.addItem("A-Admin")
        for elem in self.Controller.getListaClienti():
            if elem != self.username:
             self.cmbDestinatari.addItem("C-" + elem)
        for elem in self.Controller.getListaStaff():
            if elem != self.username:
             self.cmbDestinatari.addItem("P-" + elem)

    def scrittura_file_messaggi(self):
        esito = False
        if self.chkClienti.isChecked() == False and self.chkStaff.isChecked() == False:
            destinatario = self.cmbDestinatari.currentText().split("-")
            esito = self.Controller.spedisciMessaggio(destinatario[1], self.username, self.ptxTesto.toPlainText(),
                                              datetime.today().strftime('%Y-%m-%d-%H:%M'))
        if self.chkClienti.isChecked() == True:
            for elem in self.Controller.getListaClienti():
                esito = self.Controller.spedisciMessaggio(elem, self.username, self.ptxTesto.toPlainText(),
                                                  datetime.today().strftime('%Y-%m-%d-%H:%M'))
        if self.chkStaff.isChecked() == True:
            for elem in self.Controller.getListaStaff():
                esito = self.Controller.spedisciMessaggio(elem, self.username, self.ptxTesto.toPlainText(),
                                                  datetime.today().strftime('%Y-%m-%d-%H:%M'))
        if esito == True:
            self.objMetodi.show_popup_ok("il tuo contenuto è stato inviato correttamente")
        else:
            self.objMetodi.show_popup_exception("Impossibile mandare un messaggio vuoto.")
        self.finestra.close()

    def selezioneDestinatario(self):
        self.cmbDestinatari.setDisabled(self.Controller.selezioneDestinatario(self.chkClienti.isChecked(),
                                                                              self.chkStaff.isChecked()))

    def setupUi(self, MainWindow, username):
        self.finestra = MainWindow
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTesto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_2.setGeometry(QtCore.QRect(40, 60, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_2.setFont(font)
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.btnInviaMessaggio = QtWidgets.QPushButton(self.centralwidget)
        self.btnInviaMessaggio.setGeometry(QtCore.QRect(360, 330, 141, 28))
        self.btnInviaMessaggio.setObjectName("btnInviaMessaggio")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(30, 30, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_3.setGeometry(QtCore.QRect(20, 90, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_3.setFont(font)
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.cmbDestinatari = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDestinatari.setGeometry(QtCore.QRect(90, 60, 151, 22))
        self.cmbDestinatari.setObjectName("cmbDestinatari")
        self.ptxTesto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxTesto.setGeometry(QtCore.QRect(90, 100, 421, 211))
        self.ptxTesto.setPlainText("")
        self.ptxTesto.setObjectName("ptxTesto")
        self.lblMittente = QtWidgets.QLabel(self.centralwidget)
        self.lblMittente.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblMittente.setFont(font)
        self.lblMittente.setText("")
        self.lblMittente.setObjectName("lblMittente")
        self.chkClienti = QtWidgets.QCheckBox(self.centralwidget)
        self.chkClienti.setGeometry(QtCore.QRect(280, 60, 91, 20))
        self.chkClienti.setObjectName("chkClienti")
        self.chkStaff = QtWidgets.QCheckBox(self.centralwidget)
        self.chkStaff.setGeometry(QtCore.QRect(400, 60, 91, 20))
        self.chkStaff.setObjectName("chkStaff")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.username != "Admin":
            self.chkStaff.hide()
            self.chkClienti.hide()
        self.popola_comboBox()
        self.Controller.recuperaSalvataggio()
        self.btnInviaMessaggio.clicked.connect(self.scrittura_file_messaggi)
        self.chkStaff.clicked.connect(self.selezioneDestinatario)
        self.chkClienti.clicked.connect(self.selezioneDestinatario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrivi messaggio"))
        self.lblTesto_2.setText(_translate("MainWindow", "A:"))
        self.btnInviaMessaggio.setText(_translate("MainWindow", "Invia Messaggio"))
        self.lblTesto_1.setText(_translate("MainWindow", "DA:"))
        self.lblTesto_3.setText(_translate("MainWindow", "Oggetto:"))
        self.chkClienti.setText(_translate("MainWindow", "Tutti i clienti"))
        self.chkStaff.setText(_translate("MainWindow", "Tutto lo staff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Casella_di_messaggio()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())
