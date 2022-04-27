from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class lista_esercizi(object):

    lista_esercizi = []
    percorso = "./Cliente/Allenamenti/Data/Lista_esercizi.txt"
    objMetodi = GestioneOggetti()

    def __init__(self, username="", esercizi=""):
        if username != "":
            self.username = username
            self.esercizi = esercizi
        self.recuperaSalvataggio()

    def recuperaSalvataggio(self):
        self.lista_esercizi.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_esercizi)

    def aggiungiAllaLista(self, obj):
        self.aggiorna(obj.username)
        self.objMetodi.addToList(obj, self.lista_esercizi)
        self.scriviLista()

    def aggiorna(self, username):
        for elem in self.lista_esercizi:
            if elem.username == username:
                self.lista_esercizi.remove(elem)

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_esercizi)

    def getOggetto(self, username):
        for elem in self.lista_esercizi:
            if elem.username == username:
                return elem
        return 0

    def rimuoviOggetto(self, obj):
        for elem in self.lista_esercizi:
            if elem.username == obj.username:
                self.lista_esercizi.remove(elem)
        self.scriviLista()

    def rimuoviCliente(self, username):
        for elem in self.lista_esercizi:
            if elem.username == username:
                self.lista_esercizi.remove(elem)
        self.scriviLista()
