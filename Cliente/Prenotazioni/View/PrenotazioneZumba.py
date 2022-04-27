from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Cliente.Prenotazioni.Controller.Prenotazioni_controller import metodi_prenotazione

class prenotazione_zumba(object):
    username = ""
    objMetodi = GestioneOggetti()
    Controller = metodi_prenotazione()
    giorni_attivi = {"gio", "ven"}
    numero_massimo = 20
    sala = "Zumba"

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
        Form.resize(754, 433)
        Form.setMouseTracking(False)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(550, 220, 118, 23))
        self.progressBar.setMaximum(20)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(19, 15, 291, 61))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(550, 80, 111, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(550, 180, 111, 20))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblImmagineZumba = QtWidgets.QLabel(Form)
        self.lblImmagineZumba.setGeometry(QtCore.QRect(390, 10, 81, 71))
        self.lblImmagineZumba.setText("")
        self.lblImmagineZumba.setPixmap(QtGui.QPixmap(".\\IconaZumba.png"))
        self.lblImmagineZumba.setScaledContents(True)
        self.lblImmagineZumba.setObjectName("lblImmagineZumba")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(550, 350, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 130, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("popupcalendar")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.cmbOrario.setObjectName("cmbOrario")
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
        Form.setWindowTitle(_translate("Form", "Zumba"))
        self.lblInfo.setText(_translate("Form",
                                      "<html><head/><body><p>Le lezioni si svolgono il giovedì e il venerdì</p><p>dalle ore 18:00 e dalle ore 19:30.</p></body></html>"))
        self.lblTesto_1.setText(_translate("Form", "Seleziona data:"))
        self.lblTesto_2.setText(_translate("Form", "Seleziona orario:"))
        self.lblTesto_3.setText(_translate("Form", "Posti disponibili:"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.cmbOrario.setItemText(0, _translate("Form", "18:00-19:30"))
        self.cmbOrario.setItemText(1, _translate("Form", "19:30-21:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazione_zumba()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
