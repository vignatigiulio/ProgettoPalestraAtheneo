from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Admin.Orario.Model.Orario import Orario

class Staff(object):
    objMetodi = GestioneOggetti()
    objOrario = Orario()
    lista_staff = []
    percorso = "./Admin/Staff/Data/CredenzialiStaff.txt"

    def __init__(self, nome="", cognome="", codice_fiscale="", ore="", mansione="", password="Atheneo2022"):
        if nome != "" or cognome != "":
            self.nome = nome
            self.cognome = cognome
            self.codice_fiscale = codice_fiscale
            self.ore = ore
            self.mansione = mansione
            self.password = password

    def popolaLista(self):
        return self.objMetodi.popolaLista(self.lista_staff)

    def recuperaSalvataggio(self):
        self.lista_staff.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_staff)

    def aggiungiAllaLista(self, obj):
        self.objMetodi.addToList(obj, self.lista_staff)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_staff)

    def getAttributi(self, id):
        return self.objMetodi.getAttributi(id, self.lista_staff)

    def rimuoviDallaLista(self, stringa_da_eliminare):
        self.objMetodi.rimuovi(stringa_da_eliminare, self.lista_staff)
        self.objOrario.rimuoviStaff(stringa_da_eliminare)
        self.scriviLista()

    def reset(self, name):
        self.objMetodi.resetpassword(name, self.lista_staff)
        self.scriviLista()

    def getClCred(self):
        return self.objMetodi.getUserPass(self.lista_staff)

    def getObject(self, id):
        return self.objMetodi.getObject(id, self.lista_staff)

    def get_lista(self):
        return self.objMetodi.get_lista(self.lista_staff)

    def controlloUnicita(self, codice_fiscale):
        for elem in self.lista_staff:
            if elem.codice_fiscale.lower() == codice_fiscale.lower():
                return False
        return True