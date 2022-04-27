from Gestione_posta_e_account.Posta.Model.Messaggio import Messaggio
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QComboBox, QLabel, QDoubleSpinBox, QStatusBar, QPushButton, \
    QPlainTextEdit
from Admin.Orario.Model.Orario import Orario
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Admin.Orario.Controller.Gestione_orari_controller import metodi_gestione_orari


class GestioneOrari(object):
    Controller = metodi_gestione_orari()
    objMetodi = GestioneOggetti()
    username = ""
    objOrario = Orario()
    objMessaggio = Messaggio()
    validita_giorno = False

    def fasciaOraria(self):
        vettore_orari = self.Controller.fasciaOraria(self.cmbTipo.currentText())
        self.cmbFasciaOraria.clear()
        for elem in vettore_orari:
            self.cmbFasciaOraria.addItem(elem)

    def controllaGiorno(self):
        self.ptxCasella.clear()
        if self.Controller.controllaGiorno(self.cmbTipo.currentText(),
                                           self.calendarWidget.selectedDate().toString()[:3]):
            self.controllaTurno()
            self.validita_giorno = True
        else:
            self.objMetodi.show_popup_exception("Selezionare un giorno corretto.")
            self.validita_giorno = False

    def salva(self):
        if self.calendarWidget.selectedDate().toString() != "" and self.validita_giorno:
            if self.Controller.salva(self.calendarWidget.selectedDate().toString(), self.cmbFasciaOraria.currentText(),
                                  self.username, self.spbPaga.text(), self.cmbTipo.currentText()):
                self.controllaTurno()
                self.objMetodi.show_popup_ok("Salvato con successo.")
            else:
                self.objMetodi.show_popup_exception("Esiste già un turno uguale.")
        else:
            self.objMetodi.show_popup_exception("Selezionare una data.")

    def controllaTurno(self):
        self.ptxCasella.clear()
        listaprenotati = self.Controller.restituisciListaControllaTurno(self.calendarWidget.selectedDate().toString())
        for elem in listaprenotati:
            self.ptxCasella.appendPlainText(
                "In data " + elem.data + " dalle " + elem.orario +
                " nella sala " + elem.tipo + " è presente " + elem.staff)

    def rimuoviGiornata(self):
        if self.Controller.presenzaTurno(self.username, self.calendarWidget.selectedDate().toString()):
            if self.objMetodi.show_popup_question("Verrà rimosso il turno di " + self.username + " dalla giornata di " +
                                                  self.calendarWidget.selectedDate().toString() + " delle " +
                                                  self.cmbFasciaOraria.currentText()+" di " + self.cmbTipo.currentText() + ". Continuare?"):
                self.Controller.rimuoviTurno(self.username, self.calendarWidget.selectedDate().toString(),
                                             self.cmbFasciaOraria.currentText(), self.cmbTipo.currentText())

                self.controllaTurno()
                self.objMetodi.show_popup_ok("Rimosso con successo.")
        else:
            self.objMetodi.show_popup_exception("Impossibile trovare " + self.username + " nella giornata di "
                                                + self.calendarWidget.selectedDate().toString())
            self.controllaTurno()

    def setupUi(self, MainWindow, username):
        self.username = username
        MainWindow.resize(900, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 30, 280, 240))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.cmbTipo = QComboBox(self.centralwidget)
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.setObjectName(u"cmbTipo")
        self.cmbTipo.setGeometry(QRect(380, 90, 131, 22))
        self.cmbTipo.setEditable(True)
        self.ptxCasella = QPlainTextEdit(self.centralwidget)
        self.ptxCasella.setObjectName(u"ptxCasella")
        self.ptxCasella.setGeometry(QRect(40, 280, 701, 331))
        self.ptxCasella.setReadOnly(True)
        self.spbPaga = QDoubleSpinBox(self.centralwidget)
        self.spbPaga.setObjectName(u"spbPaga")
        self.spbPaga.setGeometry(QRect(410, 130, 62, 22))
        self.spbPaga.setDecimals(1)
        self.lblPagaOrario = QLabel(self.centralwidget)
        self.lblPagaOrario.setObjectName(u"lblPagaOrario")
        self.lblPagaOrario.setGeometry(QRect(330, 130, 61, 21))
        self.lblTitolo = QLabel(self.centralwidget)
        self.lblTitolo.setObjectName(u"lblTitolo")
        self.lblTitolo.setGeometry(QRect(40, 10, 251, 16))
        self.lblTitolo.setAlignment(Qt.AlignCenter)
        self.btnSalva = QPushButton(self.centralwidget)
        self.btnSalva.setObjectName(u"btnSalva")
        self.btnSalva.setGeometry(QRect(330, 170, 75, 24))
        self.btnRimuovi = QPushButton(self.centralwidget)
        self.btnRimuovi.setObjectName(u"btnRimuovi")
        self.btnRimuovi.setGeometry(QRect(330, 220, 75, 24))
        self.lblCompensi = QLabel(self.centralwidget)
        self.lblCompensi.setObjectName(u"lblCompensi")
        self.lblCompensi.setGeometry(QRect(500, 130, 231, 16))
        self.lblTesto_1 = QLabel(self.centralwidget)
        self.lblTesto_1.setObjectName(u"lblTesto_1")
        self.lblTesto_1.setGeometry(QRect(330, 20, 31, 20))
        self.lblTesto_2 = QLabel(self.centralwidget)
        self.lblTesto_2.setObjectName(u"lblTesto_2")
        self.lblTesto_2.setGeometry(QRect(328, 90, 41, 20))
        self.cmbFasciaOraria = QComboBox(self.centralwidget)
        self.cmbFasciaOraria.setObjectName(u"cmbInizio")
        self.cmbFasciaOraria.setGeometry(QRect(380, 20, 131, 22))
        self.cmbFasciaOraria.setEditable(True)
        self.fasciaOraria()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.fasciaOraria()
        self.lblTitolo.setText(self.username)
        self.cmbTipo.activated.connect(self.fasciaOraria)
        self.calendarWidget.setMinimumDate(QDate.currentDate())
        self.calendarWidget.setMaximumDate(QDate.currentDate().addMonths(3))
        self.calendarWidget.clicked.connect(self.controllaGiorno)
        self.btnSalva.clicked.connect(self.salva)
        self.objOrario.recuperaSalvataggio()
        self.btnRimuovi.clicked.connect(self.rimuoviGiornata)
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.controllaTurno()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestione turni", None))
        _translate = QtCore.QCoreApplication.translate
        self.cmbTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Sala Pesi", None))
        self.cmbTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Zumba", None))
        self.cmbTipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Functional", None))
        self.lblPagaOrario.setText(QCoreApplication.translate("MainWindow", u"Paga oraria", None))
        self.lblTitolo.setText("")
        self.btnSalva.setText(QCoreApplication.translate("MainWindow", u"Salva", None))
        self.btnRimuovi.setText(QCoreApplication.translate("MainWindow", u"Rimuovi", None))
        self.lblCompensi.setText("")
        self.ptxCasella.setPlainText(_translate("MainWindow", "Seleziona un giorno dal calendario."))
        self.lblTesto_1.setText(QCoreApplication.translate("MainWindow", u"Da", None))
        self.lblTesto_2.setText(QCoreApplication.translate("MainWindow", u"Sala", None))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GestioneOrari()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())
