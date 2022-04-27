from Gestione_allenamento.Model.Scheda_esercizi import Esercizi


class metodi_scheda_allenamento(object):
    Model = Esercizi()

    def creaOggetto(self, username, nome_esercizi, numero_esercizi, data_inizio, data_fine):
        self.objScheda = Esercizi(username, nome_esercizi, numero_esercizi, data_inizio, data_fine)

    def controlloData(self):
        return self.Model.confrontaData(self.objScheda)

    def sovrascrivi(self):
        self.Model.rimuoviOggetto(self.objScheda)
        self.Model.aggiungiAllaLista(self.objScheda)

    def scrivi(self):
        self.Model.aggiungiAllaLista(self.objScheda)

    def restituisciDati(self, username):
        return self.Model.getOggetto(username)
