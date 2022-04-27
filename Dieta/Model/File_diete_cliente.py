from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class File_diete_cliente(object):

    objMetodi = GestioneOggetti()
    percorso = "./Dieta/Data/Dati_clienti.txt"
    lista_informazioni = []
    percorso_diete_assegnate = "./Dieta/Data/Files_diete_personali/"

    def __init__(self, username="", bmi="", peso_ideale="", fabbisogno="", segnalazioni=""):
        if username != "":
            self.username = username
            self.bmi = bmi
            self.peso_ideale = peso_ideale
            self.fabbisogno = fabbisogno
            self.segnalazioni = segnalazioni
        self.recuperaSalvataggio()

    def controllaRidondanza(self, username):
        for elem in self.lista_informazioni:
            if elem.username == username:
                return True
        return False

    def rimuoviOggetto(self, username):
        for elem in self.lista_informazioni:
            if elem.username == username:
                self.lista_informazioni.remove(elem)
        self.scriviLista()

    def recuperaSalvataggio(self):
        self.lista_informazioni.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_informazioni)

    def aggiungiAllaLista(self, obj):
        self.objMetodi.addToList(obj, self.lista_informazioni)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_informazioni)

    def popolaListaDieta(self):
        try:
            with open("./Dieta/Data/dieta.txt", "r") as openfile:
                lettura = openfile.read()
            lettura = lettura.split("\n")
            return lettura
        except Exception:
            return 0

    def getOggetto(self, username):
        for elem in self.lista_informazioni:
            if elem.username == username:
                return elem
        return 0

    def rimuoviFilesDietaAssegnato(self, username):
        lista_files_dieta = self.objMetodi.getListaFiles(self.percorso_diete_assegnate)
        for elem in lista_files_dieta:
            if elem.startswith(username):
                self.objMetodi.rimuoviFiles(self.percorso_diete_assegnate+elem)
