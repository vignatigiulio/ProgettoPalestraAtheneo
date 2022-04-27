from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Cliente.Prenotazioni.Controller.Prenotazioni_controller import metodi_prenotazione

class prenotazioni_allenamento_functional(object):

    Controller = metodi_prenotazione()
    username = ""
    objMetodi = GestioneOggetti()
    giorni_attivi = {"mar", "mer", "ven"}
    numero_massimo = 15
    sala = "Allenamento Functional"

    def prenota(self):

        if self.Controller.controlloApertura(self.popupcalendar.selectedDate(), self.giorni_attivi):
            if self.Controller.prenota(self.numero_massimo,
                                       self.Controller.creaOggettoPrenotazione(self.username, self.sala,
                                                                               self.popupcalendar.selectedDate(),
                                                                               self.cmbOrario.currentText())):
                self.objMetodi.show_popup_ok("Prenotazione effetuata.")
            else:
                self.objMetodi.show_popup_exception("Prenotazione già effettuata o limite massimo raggiunto.")
            self.finestra.close()
        else:
            self.objMetodi.show_popup_exception("Selezionare un giorno corretto.")

    def cmbAttive(self):
        if self.Controller.controlloApertura(self.popupcalendar.selectedDate(), self.giorni_attivi):
            self.progressBar.setValue(self.Controller.getNumeroInSala(self.sala, self.popupcalendar.selectedDate(),
                                                                      self.cmbOrario.currentText()))

    def eliminaVecchiePrenotazioni(self):
        self.Controller.pulisciPrenotazioni()

    def setupUi(self, Form, username):
        self.finestra = Form
        self.username = username
        Form.setObjectName("Form")
        Form.resize(756, 411)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(560, 230, 121, 23))
        self.progressBar.setMaximum(15)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(560, 340, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(0, 100, 111, 16))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(550, 80, 111, 20))
        self.lblTesto_1.setObjectName("lblTesto_2")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(560, 200, 81, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(19, 15, 311, 61))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblImmagineFunctional = QtWidgets.QLabel(Form)
        self.lblImmagineFunctional.setGeometry(QtCore.QRect(370, 10, 91, 71))
        self.lblImmagineFunctional.setText("")
        self.lblImmagineFunctional.setPixmap(QtGui.QPixmap(".\\IconaAllFunzionale.png"))
        self.lblImmagineFunctional.setScaledContents(True)
        self.lblImmagineFunctional.setObjectName("lblImmagineFunctional")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 120, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("popupcalendar")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.cmbOrario.setObjectName("cmbOrari")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnPrenota.clicked.connect(self.prenota)
        self.popupcalendar.setMinimumDate(QDate.currentDate())
        self.cmbOrario.activated[str].connect(self.cmbAttive)
        self.popupcalendar.clicked.connect(self.cmbAttive)
        self.popupcalendar.setMaximumDate(QDate.currentDate().addMonths(1))
        self.eliminaVecchiePrenotazioni()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prenotazioni functional"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.lblInfo.setText(_translate("Form", "Seleziona data:"))
        self.lblTesto_1.setText(_translate("Form", "Seleziona orario:"))
        self.lblTesto_2.setText(_translate("Form", "Posti liberi:"))
        self.lblTesto_3.setText(_translate("Form",
                                        "<html><head/><body><p>Le lezioni di Allenamento Funzionale si svolgono<br/>martedì, mercoledì e venerdì.<br/>Dalle ore 15:30 e dalle 17:00. <br/></p></body></html>"))
        self.cmbOrario.setItemText(0, _translate("Form", "15:30-17:00"))
        self.cmbOrario.setItemText(1, _translate("Form", "17:00-18:30"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni_allenamento_functional()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
