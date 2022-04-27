from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti

class Orario(object):
    lista_turni = []
    objMetodi = GestioneOggetti()
    percorso = "./Admin/Orario/Data/TurniStaff.txt"

    def __init__(self, data ="", orario="", staff="", paga="", tipo=""):
        self.recuperaSalvataggio()
        if data != "":
            self.data = data
            self.orario = orario
            self.staff = staff
            self.paga = paga
            self.tipo = tipo

    def recuperaSalvataggio(self):
        self.lista_turni.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_turni)

    def addToList(self, obj):
        if self.objMetodi.confrontaTurno(obj, self.lista_turni):
            return False
        else:
            self.objMetodi.addToList(obj, self.lista_turni)
            self.scriviLista()
            return True

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_turni)

    def controlloGiorno(self, data):
        return self.objMetodi.controlloGiorno(data, self.lista_turni)

    def controlloLavoro(self, data, staff):
        return self.objMetodi.controlloLavoro(data, staff, self.lista_turni)

    def rimuoviTurno(self, username, data, tipo, orario):
        self.objMetodi.rimuoviTurno(username, data, tipo, orario, self.lista_turni, self.percorso)

    def rimuoviStaff(self, username):
        for elem in self.lista_turni:
            if elem.staff == username:
                self.lista_turni.remove(elem)
        self.scriviLista()