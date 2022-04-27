import os

from Cliente.Prenotazioni.Model.Prenotazioni import GestionePrenotazioniCorsi

class metodi_prenotazione(object):
    Model = GestionePrenotazioniCorsi()

    def creaOggettoPrenotazione(self, username, sala, data, orario):
        objPrenotazione = GestionePrenotazioniCorsi(username, sala, data, orario)
        return objPrenotazione

    def prenota(self, numero_massimo, objPrenotazione):
        return self.Model.prenota(numero_massimo, objPrenotazione)

    def getNumeroInSala(self, sala, data, ora):
        return self.Model.getNumeroInSala(sala, data, ora)

    def controlloApertura(self, data_selezionata, giorni_attivi):
        for elem in giorni_attivi:
            if data_selezionata.toString()[:3] == elem:
                return True
        return False

    def pulisciPrenotazioni(self):
        self.Model.eliminaVecchiePrenotazioni()

    def controlloCapienza(self, percorso):
        if os.path.exists(percorso):
            with open(percorso, "r") as openfile:
                lettura = openfile.readlines()
            return len(lettura)
        else:
            return 0
