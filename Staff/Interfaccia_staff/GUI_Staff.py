import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from os import listdir
from os.path import isfile, join
from Gestione_posta_e_account.Posta.View.Casella_di_messaggio import Casella_di_messaggio
from Gestione_posta_e_account.Posta.View.Leggi_messaggio import lettura_messaggio
from Gestione_posta_e_account.Cambio_password.View.Cambio_password import change_password
from Admin.Cliente.Model.Cliente import Cliente
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Gestione_posta_e_account.Posta.Model.Messaggio import Messaggio
from Admin.Orario.Model.Orario import Orario
from Gestione_allenamento.View.Scheda_allenamento import allenamento_staff
from Dieta.View.Scheda_dieta import dieta_staff
from Cliente.Allenamenti.Model.Allenamento import lista_esercizi
from Dieta.Model.File_diete_cliente import File_diete_cliente

class GUI_staff(object):
    objEsercizipreferiti = lista_esercizi()
    objOrario = Orario()
    objCliente = Cliente()
    username = ""
    username_cliente = ""
    messaggio = Messaggio()
    objMetodi = GestioneOggetti()
    lista_messaggi = []
    lista_file_utente = []
    objInfoCliente = File_diete_cliente()
    percorso = "./Dieta/Data/Files_diete_personali/"

    def carica(self):
        self.listWidget_allenamento.clear()
        l = self.objCliente.popolaLista()
        if l is not None:
            for x in l:
                self.listWidget_allenamento.addItem(x)
                self.listWidget_dieta.addItem(x)
        self.listWidget_esercizi.hide()
        self.listWidget_dati.hide()

    def open(self):
        try:
            for elem in [f for f in listdir(self.percorso) if isfile(join(self.percorso, f))]:
                if elem.startswith(self.listWidget_dieta.currentItem().text().replace(" ", "")):
                    os.chdir(self.percorso)
                    os.system(elem)
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("..")
                    return
            self.objMetodi.show_popup_exception("File non trovato.")
        except(Exception):
            self.objMetodi.show_popup_exception("Errore nell'apertura della dieta.")

    def visualizza_esercizi(self):
        self.listWidget_esercizi.show()
        self.listWidget_esercizi.clear()
        oggetto_scheda_preferiti = \
            self.objEsercizipreferiti.getOggetto(self.listWidget_allenamento.currentItem().text().replace(" ", ""))
        if oggetto_scheda_preferiti != 0:
            for elem in oggetto_scheda_preferiti.esercizi:

                self.listWidget_esercizi.addItem(elem)
        else:
            self.listWidget_esercizi.addItem("Nessun esercizio selezionato dal cliente")


    def orario(self):
        self.ptxTestoOrario.clear()
        lavoro = self.objOrario.controlloLavoro(self.calendarWidget.selectedDate().toString(), self.username)
        for elem in lavoro:
            self.ptxTestoOrario.appendPlainText(
                "In data " + elem.data + " ti occuperai di " + elem.tipo + " alle " +
                elem.orario + "\n")

    def visualizza_messaggi(self):
        self.listWidget_messaggi.clear()
        self.lista_messaggi = self.messaggio.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.listWidget_messaggi.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.listWidget_messaggi.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def open_window_leggi_messaggio(self):

        self.lettura_messaggio = QtWidgets.QMainWindow()
        self.ui = lettura_messaggio()
        self.ui.setupUi(self.lettura_messaggio, self.messaggio, self.username)
        self.lettura_messaggio.show()

    def open_window_allenamento_staff(self):
        try:
            self.username_cliente = self.listWidget_allenamento.currentItem().text()
            self.allenamento_staff = QtWidgets.QMainWindow()
            self.ui = allenamento_staff()
            self.ui.setupUi(self.allenamento_staff, self.username_cliente)
            self.allenamento_staff.show()
        except(Exception):
            self.objMetodi.show_popup_exception("Non hai selezionato nulla nella lista!")

    def open_window_password(self):
        self.password = QtWidgets.QMainWindow()
        self.ui = change_password()
        self.ui.setupUi(self.password, self.username)
        self.password.show()

    def open_window_message(self):
        self.casella_messaggi = QtWidgets.QMainWindow()
        self.ui = Casella_di_messaggio()
        self.ui.setupUi(self.casella_messaggi, self.username)
        self.casella_messaggi.show()

    def open_window_dieta_staff(self):
        if self.objInfoCliente.getOggetto(self.listWidget_dieta.currentItem().text().replace(" ", "")) != 0:
            self.dieta_staff = QtWidgets.QMainWindow()
            self.ui = dieta_staff()
            self.ui.setupUi(self.dieta_staff, self.listWidget_dieta.currentItem().text().replace(" ", ""))
            self.dieta_staff.show()
        else:
            self.objMetodi.show_popup_exception("Il cliente deve prima indicare i dati fisiologici.")

    def return_message(self):
        riga = self.listWidget_messaggi.currentRow()
        lista_messaggi_destinatario = self.messaggio.getObject_message(self.username)
        lista_messaggi_destinatario.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        self.messaggio = lista_messaggi_destinatario[riga]
        self.open_window_leggi_messaggio()

    def elimina_messaggio(self):

        messaggio = self.lista_messaggi[self.listWidget_messaggi.currentRow()]
        self.messaggio.rimuovi_messaggio(messaggio)
        self.listWidget_messaggi.takeItem(self.listWidget_messaggi.currentRow())
        self.visualizza_messaggi()

    def nascondi_dieta(self):
        self.listWidget_dati.hide()
        self.label_8.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.txtPesoForma.hide()
        self.txtBmi.hide()
        self.txtFabbisogno.hide()

    def appari_dieta(self):
        self.listWidget_dati.show()
        self.label_8.show()
        self.label_7.show()
        self.label_9.show()
        self.txtPesoForma.show()
        self.txtBmi.show()
        self.txtFabbisogno.show()

    def check_indici_fisiologici(self):
        oggetto_dati = self.objInfoCliente.getOggetto(self.listWidget_dieta.currentItem().text().replace(" ", ""))
        self.txtBmi.clear()
        self.txtPesoForma.clear()
        self.txtFabbisogno.clear()
        self.nascondi_dieta()
        if oggetto_dati != 0:
            self.appari_dieta()
            self.txtBmi.setText(oggetto_dati.bmi)
            self.txtPesoForma.setText(oggetto_dati.peso_ideale)
            self.txtFabbisogno.setText(oggetto_dati.fabbisogno)

    def setupUi(self, MainWindow, username):
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(90, 40, 701, 531))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page.setObjectName("page")
        self.listWidget_allenamento = QtWidgets.QListWidget(self.page)
        self.listWidget_allenamento.setGeometry(QtCore.QRect(20, 10, 201, 391))
        self.listWidget_allenamento.setObjectName("listWidget")
        self.listWidget_esercizi = QtWidgets.QListWidget(self.page)
        self.listWidget_esercizi.setGeometry(QtCore.QRect(320, 70, 291, 171))
        self.listWidget_esercizi.setAcceptDrops(False)
        self.listWidget_esercizi.setObjectName("listWidget_2")
        self.btnCreaScheda = QtWidgets.QPushButton(self.page)
        self.btnCreaScheda.setGeometry(QtCore.QRect(412, 370, 251, 28))
        self.btnCreaScheda.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.listWidget_allenamento.raise_()
        self.listWidget_esercizi.raise_()
        self.btnCreaScheda.raise_()
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_2.setObjectName("page_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 451, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 270, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 221, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ptxTestoOrario = QtWidgets.QPlainTextEdit(self.page_2)
        self.ptxTestoOrario.setGeometry(QtCore.QRect(180, 280, 281, 91))
        self.ptxTestoOrario.setObjectName("ptxTestoOrario")
        self.ptxTestoOrario.setReadOnly(True)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.calendarWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.ptxTestoOrario.raise_()
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_3.setObjectName("page_3")
        self.listWidget_dieta = QtWidgets.QListWidget(self.page_3)
        self.listWidget_dieta.setGeometry(QtCore.QRect(10, 10, 201, 391))
        self.listWidget_dieta.setObjectName("listWidget_3")
        self.listWidget_dati = QtWidgets.QListWidget(self.page_3)
        self.listWidget_dati.setGeometry(QtCore.QRect(290, 50, 256, 192))
        self.listWidget_dati.setObjectName("listWidget_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(320, 190, 81, 20))
        self.label_7.setObjectName("label_7")
        self.txtPesoForma = QtWidgets.QLineEdit(self.page_3)
        self.txtPesoForma.setGeometry(QtCore.QRect(410, 150, 113, 21))
        self.txtPesoForma.setObjectName("lineEdit_5")
        self.txtPesoForma.setReadOnly(True)
        self.txtBmi = QtWidgets.QLineEdit(self.page_3)
        self.txtBmi.setGeometry(QtCore.QRect(410, 110, 113, 21))
        self.txtBmi.setObjectName("lineEdit_6")
        self.txtBmi.setReadOnly(True)
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(320, 150, 81, 20))
        self.label_8.setObjectName("label_8")
        self.txtFabbisogno = QtWidgets.QLineEdit(self.page_3)
        self.txtFabbisogno.setGeometry(QtCore.QRect(410, 190, 113, 21))
        self.txtFabbisogno.setObjectName("lineEdit_7")
        self.txtFabbisogno.setReadOnly(True)
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(320, 110, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(360, 70, 111, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btnCreaDieta = QtWidgets.QPushButton(self.page_3)
        self.btnCreaDieta.setGeometry(QtCore.QRect(470, 370, 121, 28))
        self.btnCreaDieta.setObjectName("pushButton_5")
        self.btnApriDieta = QtWidgets.QPushButton(self.page_3)
        self.btnApriDieta.setGeometry(QtCore.QRect(470, 330, 121, 28))
        self.btnApriDieta.setObjectName("btnApriDieta")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.listWidget_dieta.raise_()
        self.listWidget_dati.raise_()
        self.label_7.raise_()
        self.txtPesoForma.raise_()
        self.txtBmi.raise_()
        self.label_8.raise_()
        self.txtFabbisogno.raise_()
        self.label_9.raise_()
        self.label_3.raise_()
        self.btnCreaDieta.raise_()
        self.btnApriDieta.raise_()
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_4.setObjectName("page_4")
        self.listWidget_messaggi = QtWidgets.QListWidget(self.page_4)
        self.listWidget_messaggi.setGeometry(QtCore.QRect(70, 90, 441, 251))
        self.listWidget_messaggi.setObjectName("listWidget_4")
        self.btnAggiornaMex = QtWidgets.QPushButton(self.page_4)
        self.btnAggiornaMex.setGeometry(QtCore.QRect(475, 95, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiornaMex.setText("")
        self.btnAggiornaMex.setIcon(icon)
        self.btnAggiornaMex.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMex.setObjectName("btnAggiornaMex")
        self.btnApriMessaggio = QtWidgets.QPushButton(self.page_4)
        self.btnApriMessaggio.setGeometry(QtCore.QRect(530, 210, 141, 28))
        self.btnApriMessaggio.setObjectName("pushButton_7")
        self.btnEliminaMessaggio = QtWidgets.QPushButton(self.page_4)
        self.btnEliminaMessaggio.setGeometry(QtCore.QRect(530, 260, 141, 28))
        self.btnEliminaMessaggio.setObjectName("pushButton_8")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnPassword = QtWidgets.QPushButton(self.page_4)
        self.btnPassword.setGeometry(QtCore.QRect(530, 300, 141, 28))
        self.btnPassword.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(480, 0, 101, 71))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("./Resources/images/images.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_6.raise_()
        self.listWidget_messaggi.raise_()
        self.btnApriMessaggio.raise_()
        self.btnEliminaMessaggio.raise_()
        self.btnAggiornaMex.raise_()
        self.label_5.raise_()
        self.btnPassword.raise_()
        self.label_13.raise_()
        self.toolBox.addItem(self.page_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.messaggio.recuperaSalvataggio()
        self.visualizza_messaggi()
        self.btnCreaDieta.hide()
        self.btnApriDieta.hide()
        self.carica()
        self.nascondi_dieta()
        self.listWidget_dieta.clicked.connect(self.check_indici_fisiologici)
        self.listWidget_dieta.clicked.connect(self.btnCreaDieta.show)
        self.listWidget_dieta.clicked.connect(self.btnApriDieta.show)
        self.listWidget_allenamento.clicked.connect(self.visualizza_esercizi)
        self.btnCreaScheda.clicked.connect(self.open_window_allenamento_staff)
        self.btnPassword.clicked.connect(self.open_window_password)
        self.btnApriMessaggio.clicked.connect(self.open_window_message)
        self.listWidget_messaggi.doubleClicked.connect(self.return_message)
        self.btnEliminaMessaggio.clicked.connect(self.elimina_messaggio)
        self.btnCreaDieta.clicked.connect(self.open_window_dieta_staff)
        self.objOrario.recuperaSalvataggio()
        self.calendarWidget.clicked.connect(self.orario)
        self.calendarWidget.setMinimumDate(QDate.currentDate())
        self.calendarWidget.setMaximumDate(QDate.currentDate().addMonths(3))
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.orario()
        self.btnApriDieta.clicked.connect(self.open)
        self.btnAggiornaMex.clicked.connect(self.visualizza_messaggi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Istruttore "+self.username))
        self.btnCreaScheda.setText(_translate("MainWindow", "Crea scheda di allenamento"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Allenamento"))
        self.label.setText(_translate("MainWindow", "Il tuo orario lavorativo:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Orario"))
        self.label_7.setText(_translate("MainWindow", "FABBISOGNO"))
        self.label_8.setText(_translate("MainWindow", "PESO FORMA:"))
        self.label_9.setText(_translate("MainWindow", "BMI:"))
        self.btnCreaDieta.setText(_translate("MainWindow", "Crea una dieta"))
        self.btnApriDieta.setText(_translate("MainWindow", "Apri dieta"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Dieta"))
        self.btnApriMessaggio.setText(_translate("MainWindow", "Scrivi Messaggio"))
        self.btnEliminaMessaggio.setText(_translate("MainWindow", "Elimina Messaggio"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">BACHECA MESSAGGI</span></p><p align=\"center\"><span style=\" color:#55aa00;\"><br/></span></p></body></html>"))
        self.btnPassword.setText(_translate("MainWindow", "Cambia password"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Bacheca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_staff()
    ui.setupUi(MainWindow,username="")
    MainWindow.show()
    sys.exit(app.exec_())
