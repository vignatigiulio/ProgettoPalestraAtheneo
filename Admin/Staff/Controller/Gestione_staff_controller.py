from Admin.Staff.Model.Staff import Staff
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class metodi_gestione_staff(object):

    objStaff = Staff()
    objMetodi = GestioneOggetti()

    def salva(self, nome, cognome, codice_fiscale, ore, titolo):
        self.objStaff = Staff(nome, cognome, codice_fiscale, ore, titolo)
        self.objStaff.aggiungiAllaLista(self.objStaff)

    def restituisciOggetto(self, nome):
        return self.objStaff.getAttributi(nome)

    def rimuoviDallaLista(self, nome):
        self.objStaff.rimuoviDallaLista(nome)

    def aggiungiAllaLista(self, oggetto):
        self.objStaff.aggiungiAllaLista(oggetto)

    def eliminaPersonale(self, nome):
        if self.objMetodi.show_popup_question("Sei sicuro di voler eliminare il membro dello staff? "
                                              "Verranno rimossi anche i suoi turni di lavoro."):
            self.objStaff.rimuoviDallaLista(nome)

    def resetPassword(self, nome):
        self.objStaff.reset(nome)


