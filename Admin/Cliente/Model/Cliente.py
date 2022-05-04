from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Admin.Abbonamento.Model.Abbonamento import Abbonamento
from Cliente.Prenotazioni.Model.Prenotazioni import GestionePrenotazioniCorsi
from Cliente.Allenamenti.Model.Allenamento import lista_esercizi
from Dieta.Model.File_diete_cliente import File_diete_cliente
from Gestione_allenamento.Model.Scheda_esercizi import Esercizi

class Cliente(object):
    objAbbonamento = Abbonamento()
    lista_clienti = []
    objMetodi = GestioneOggetti()
    percorso = "./Admin/Cliente/Data/CredenzialiClienti.txt"
    objPrenotazioni = GestionePrenotazioniCorsi()
    objPreferenze = lista_esercizi()
    objDieta = File_diete_cliente()
    objSchedaEsercizi = Esercizi()

    def __init__(self, nome="", cognome="", sesso="", data_di_nascita="", luogo_di_nascita="", codice_fiscale="",
                 password="Atheneo2022", Abbonamento="", altezza="", peso="", eta=""):
        if nome != "" or cognome != "":
            self.nome = nome
            self.cognome = cognome
            self.sesso = sesso
            self.data_nascita = data_di_nascita
            self.luogo_nascita = luogo_di_nascita
            self.codice_fiscale = codice_fiscale
            self.password = password
            self.objAbbonamento = Abbonamento
            self.altezza = altezza
            self.peso = peso
            self.eta = eta

    def popolaLista(self):
        return self.objMetodi.popolaLista(self.lista_clienti)

    def recuperaSalvataggio(self):
        self.lista_clienti.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_clienti)

    def aggiungiAllaLista(self, obj):
        self.objMetodi.addToList(obj, self.lista_clienti)
        self.scriviLista()

    def rimuoviDallaLista(self, stringa_da_eliminare):
        self.objMetodi.rimuovi(stringa_da_eliminare, self.lista_clienti)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_clienti)

    def elimina(self, stringa_da_eliminare):
        self.objMetodi.rimuovi(stringa_da_eliminare, self.lista_clienti)
        self.objPrenotazioni.rimuoviCliente(stringa_da_eliminare.replace(" ", ""))
        self.objPreferenze.rimuoviCliente(stringa_da_eliminare.replace(" ", ""))
        self.objDieta.rimuoviOggetto(stringa_da_eliminare.replace(" ", ""))
        self.objDieta.rimuoviFilesDietaAssegnato(stringa_da_eliminare.replace(" ", ""))
        self.objSchedaEsercizi.rimuoviCliente(stringa_da_eliminare.replace(" ", ""))
        self.scriviLista()

    def getAttributi(self, id):
        return self.objMetodi.getAttributi(id, self.lista_clienti)

    def getObject(self, id):
        return self.objMetodi.getObject(id, self.lista_clienti)

    def getClCred(self):
        return self.objMetodi.getUserPass(self.lista_clienti)

    def reset(self, name):
        self.objMetodi.resetpassword(name, self.lista_clienti)
        self.scriviLista()

    def get_lista(self):
        return self.objMetodi.get_lista(self.lista_clienti)

    def getSesso(self, oggetto_cliente):
        return oggetto_cliente.sesso

    def getEta(self, oggetto_cliente):
        return oggetto_cliente.eta

    def getPeso(self, oggetto_cliente):
        return oggetto_cliente.peso

    def getAltezza(self, oggetto_cliente):
        return oggetto_cliente.altezza

    def controllaUnicita(self, codice_fiscale):
        for elem in self.lista_clienti:
            if elem.codice_fiscale.lower() == codice_fiscale.lower():
                return False
        return True