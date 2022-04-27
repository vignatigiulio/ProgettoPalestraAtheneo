from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Cliente.Prenotazioni.Controller.Prenotazioni_controller import metodi_prenotazione

class prenotazioni_sala_pesi(object):

    Controller = metodi_prenotazione()
    username = ""
    objMetodi = GestioneOggetti()
    giorni_attivi = {"lun", "mar", "mer", "gio", "ven", "sab"}
    numero_massimo = 10
    sala = "Sala Pesi"

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
        Form.resize(758, 487)
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(20, 120, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("calendarWidget")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(20, 20, 351, 71))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(160, 100, 101, 16))
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(580, 110, 81, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(580, 210, 111, 16))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(580, 250, 131, 23))
        self.progressBar.setMaximum(10)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(550, 400, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.lblImmagineSalaPesi = QtWidgets.QLabel(Form)
        self.lblImmagineSalaPesi.setGeometry(QtCore.QRect(400, 10, 61, 61))
        self.lblImmagineSalaPesi.setText("")
        self.lblImmagineSalaPesi.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/IconaSalaPesi1.png"))
        self.lblImmagineSalaPesi.setScaledContents(True)
        self.lblImmagineSalaPesi.setObjectName("lblImmagineSalaPesi")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(580, 140, 111, 22))
        self.cmbOrario.setObjectName("cmbOrari")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
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
        Form.setWindowTitle(_translate("Form", "Prenotazioni sala pesi"))
        self.lblInfo.setText(_translate("Form",
                                      "<html><head/><body><p>La Sala Pesi è aperta dal lunedì al sabato. <br/>La prenotazione è valida per 1 ora e 30 minuti dall\'ora selezionata.</p></body></html>"))
        self.lblTesto_1.setText(_translate("Form", "Scegli il giorno:"))
        self.lblTesto_2.setText(_translate("Form", "Scegli l\'ora"))
        self.lblTesto_3.setText(_translate("Form", "Posti disponibili:"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.cmbOrario.setItemText(0, _translate("Form", "09:30-11:00"))
        self.cmbOrario.setItemText(1, _translate("Form", "11:00-12:30"))
        self.cmbOrario.setItemText(2, _translate("Form", "12:30-14:00"))
        self.cmbOrario.setItemText(3, _translate("Form", "14:00-15:30"))
        self.cmbOrario.setItemText(4, _translate("Form", "15:30-17:00"))
        self.cmbOrario.setItemText(5, _translate("Form", "17:00-18:30"))
        self.cmbOrario.setItemText(6, _translate("Form", "18:30-20:00"))
        self.cmbOrario.setItemText(7, _translate("Form", "20:00-21:30"))
        self.cmbOrario.setItemText(8, _translate("Form", "21:30-23:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni_sala_pesi()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
