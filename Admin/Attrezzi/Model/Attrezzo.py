from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class Attrezzo(object):
    objMetodi = GestioneOggetti()
    lista_attrezzi = []
    percorso = "./Admin/Attrezzi/Data/listaAttrezzi.txt"
    def __init__(self, descrizione="", data_acquisto="", quantita="", prezzo_unitario="", data_manutenzione=""):
        if descrizione != "":
            self.descr = descrizione
            self.data_ac = data_acquisto
            self.quantita = quantita
            self.pr_uni = prezzo_unitario
            self.data_man = data_manutenzione

    def popolaLista(self):
        return self.objMetodi.popolaListaAttrezzi(self.lista_attrezzi)

    def recuperaSalvataggio(self):
        self.lista_attrezzi.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_attrezzi)

    def addToList(self, obj):
        self.objMetodi.addToListAtt(obj, self.lista_attrezzi)
        self.objMetodi.scriviLista(self.percorso, self.lista_attrezzi)

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_attrezzi)

    def rimuovi(self, riga):
        self.objMetodi.rimuoviAttrezzo(riga, self.lista_attrezzi)
        self.scriviLista()
