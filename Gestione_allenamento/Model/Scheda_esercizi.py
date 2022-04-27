from PyQt5.QtCore import QDate

from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class Esercizi(object):

    lista_schede = []
    objMetodi = GestioneOggetti()
    percorso = "./Gestione_allenamento/Data/Schede.txt"
    def __init__(self, username="", nome_esercizi="", numeri_esercizi="", data_inizio="", data_fine=""):
        if username != "":
            self.username = username
            self.nome_esercizi = nome_esercizi
            self.numeri_esercizi = numeri_esercizi
            self.data_inizio = data_inizio
            self.data_fine = data_fine
        self.recuperaSalvataggio()

    def recuperaSalvataggio(self):
        self.lista_schede.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_schede)

    def getOggetto(self, username):
        for elem in self.lista_schede:
            if elem.username == username:
                return elem
        return 0

    def confrontaData(self, scheda):
        if self.getOggetto(scheda.username) == 0:
            return False
        elif QDate.fromString(self.getOggetto(scheda.username).data_fine, "dd/MM/yyyy") > \
                QDate.currentDate():
            return True
        else:
            return False

    def rimuoviOggetto(self, obj):
        for elem in self.lista_schede:
            if elem.username == obj.username:
                self.lista_schede.remove(elem)

    def aggiungiAllaLista(self, obj):
        self.objMetodi.addToList(obj, self.lista_schede)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_schede)

    def rimuoviCliente(self, username):
        for elem in self.lista_schede:
            if elem.username == username:
                self.lista_schede.remove(elem)
        self.scriviLista()