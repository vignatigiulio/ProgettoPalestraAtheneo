from Admin.Cliente.Model.Cliente import Cliente
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Admin.Abbonamento.Model.Abbonamento import Abbonamento

class metodi_gestione_cliente(object):
    objCliente = Cliente()
    objMetodi = GestioneOggetti()
    objAbbonamento = Abbonamento()

    def salva(self, nome, cognome, luogo_nascita, codice_fiscale, sesso, data_nascita):
        password = "Atheneo2022"
        oggetto_abbonamento = self.objAbbonamento.getObj()
        objCliente = Cliente(nome.replace(" ", ""), cognome.replace(" ", ""), sesso, data_nascita, luogo_nascita,
                             codice_fiscale, password, oggetto_abbonamento)
        objCliente.aggiungiAllaLista(objCliente)
        objCliente.scriviLista()

    def controllaUnicita(self, codice_fiscale):
        return self.objCliente.controllaUnicita(codice_fiscale)

    def restituisciOggetto(self, nome):
        return self.objCliente.getAttributi(nome)

    def rimuoviCliente(self, nome):
        self.objCliente.rimuoviDallaLista(nome)

    def aggiungiAllaLista(self, oggetto_cliente):
        self.objCliente.aggiungiAllaLista(oggetto_cliente)

    def eliminaCliente(self, nome):
        if self.objMetodi.show_popup_question("Sei sicuro di voler eliminare il cliente? Verranno rimossi"
                                              " tutti i suoi dati fatta eccezione dei messaggi."):
            self.objCliente.elimina(nome)

    def resetPassword(self, nome):
        self.objCliente.reset(nome)




