from PyQt5.QtCore import QDate
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti


class GestionePrenotazioniCorsi(object):
    lista_prenotazioni = []
    percorso = "./Cliente/Prenotazioni/Data/Prenotazioni.txt"
    objMetodi = GestioneOggetti()

    def __init__(self, username="", sala="", data="", orario=""):
        self.recuperaSalvataggio()
        if username != "":
            self.username = username
            self.sala = sala
            self.data = data
            self.orario = orario

    def recuperaSalvataggio(self):
        self.lista_prenotazioni.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_prenotazioni)

    def aggiungiAllaLista(self, obj):
        self.objMetodi.addToList(obj, self.lista_prenotazioni)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_prenotazioni)

    def getNumeroInSala(self, sala, data, ora):
        indice = 0
        for elem in self.lista_prenotazioni:
            if elem.sala == sala and elem.data == data and elem.orario == ora:
                indice += 1
        return indice

    def controllaDoppione(self, objPrenotazione):
        for elem in self.lista_prenotazioni:
            if self.confrontaOggetto(elem, objPrenotazione):
                return False
        return True

    def prenota(self, limite_massimo, objPrenotazione):
        if self.getNumeroInSala(objPrenotazione.sala, objPrenotazione.data, objPrenotazione.orario) < limite_massimo and \
                self.controllaDoppione(objPrenotazione):
            self.aggiungiAllaLista(objPrenotazione)
            return True
        return False

    def eliminaVecchiePrenotazioni(self):
        for elem in self.lista_prenotazioni:
            if QDate.currentDate() > elem.data:
                self.lista_prenotazioni.remove(elem)
        self.scriviLista()

    def rimuoviOggetto(self, objPrenotazione):
        for elem in self.lista_prenotazioni:
            if self.confrontaOggetto(elem, objPrenotazione):
                self.lista_prenotazioni.remove(elem)
        self.scriviLista()

    def rimuoviCliente(self, username):
        for elem in self.lista_prenotazioni:
            if username == elem.username:
                self.lista_prenotazioni.remove(elem)
        self.scriviLista()

    def trovaCliente(self, utente):
        vettore_risposta = []
        for elem in self.lista_prenotazioni:
            if elem.username == utente:
                vettore_risposta.append(elem)
        return vettore_risposta

    def confrontaOggetto(self, obj1, obj2):
        if obj1.username == obj2.username and \
                obj1.data.toString("dd/MM/yyyy") == obj2.data.toString("dd/MM/yyyy") and \
                obj1.sala == obj2.sala and obj1.orario == obj2.orario:
            return True
        return False

    def getOggetto(self, username):
        for elem in self.lista_prenotazioni:
            if elem.username == username:
                return elem
        return 0
