from datetime import datetime
from Admin.Orario.Model.Orario import Orario
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Gestione_posta_e_account.Posta.Model.Messaggio import Messaggio


class metodi_gestione_orari(object):
    objMessaggio = Messaggio()
    objOrario = Orario()
    objMetodi = GestioneOggetti()

    def salva(self, data, fascia_oraria, username, paga, tipo):
        objOrario = Orario(data, fascia_oraria, username, paga, tipo)
        if self.objOrario.addToList(objOrario):
            self.notifica("Admin", username.replace(" ", ""), "Ti è stato assegnato il turno in data " + data + " di " + tipo + " delle "
                      + fascia_oraria)
            return True
        return False

    def fasciaOraria(self, tipo):
        vett = []
        vett.clear()
        if tipo == "Sala Pesi":
            vett.append("09:30-11:00")
            vett.append("11:00-12:30")
            vett.append("12:30-14:00")
            vett.append("14:00-15:30")
            vett.append("15:30-17:30")
            vett.append("17:00-18:30")
            vett.append("18:30-20:00")
            vett.append("20:00-21:30")
            vett.append("21:30-23:00")
            return vett
        elif tipo == "Zumba":
            vett.append("18:00-19:30")
            vett.append("19:30-21:00")
            return vett
        else:
            vett.append("15:30-17:00")
            vett.append("17:00-18:30")
            return vett

    def controllaGiorno(self, tipo, data):
        if tipo == "Sala Pesi":
            if data == "dom":
                return False
        if tipo == "Zumba":
            if data != "gio" and data != "ven":
                return False
        elif tipo == "Functional":
            if data != "mar" and data != "mer" and data != "ven":
                return False
        return True

    def restituisciListaControllaTurno(self, data):
        return self.objOrario.controlloGiorno(data)

    def presenzaTurno(self, username, data):
        for elem in self.restituisciListaControllaTurno(data):
            if elem.staff == username:
                return True
        return False

    def rimuoviTurno(self, username, data, orario, tipo):
        self.objOrario.rimuoviTurno(username, data, tipo, orario)
        self.notifica("Admin", username.replace(" ", ""), "Il turno in data " +
                                 data + " di " + tipo + " dalle " + orario + " è stato cancellato.", )

    def notifica(self, mittente, destinatario, testo):
        self.objMessaggio.notificaTurno(mittente, destinatario, testo, datetime.today().strftime('%Y-%m-%d-%H:%M'))
