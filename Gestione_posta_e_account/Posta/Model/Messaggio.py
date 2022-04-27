from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti


class Messaggio(object):
    percorso = "./Gestione_posta_e_account/Posta/Data/messaggi.txt"
    lista_messaggi = []
    objMetodi = GestioneOggetti()

    def __init__(self, mittente = "", destinatario ="", contenuto = "", data = ""):
        self.mittente = mittente
        self.destinatario = destinatario
        self.contenuto = contenuto
        self.data = data

    def popolaLista(self):
        return self.objMetodi.popolaLista(self.lista_messaggi)

    def recuperaSalvataggio(self):
        self.lista_messaggi.clear()
        self.objMetodi.recuperaSalvataggio(self.percorso, self.lista_messaggi)

    def addToList(self, obj):
        self.objMetodi.addToList(obj, self.lista_messaggi)
        self.scriviLista()

    def scriviLista(self):
        self.objMetodi.scriviLista(self.percorso, self.lista_messaggi)

    def rimuovi_messaggio(self, obj):
        self.objMetodi.rimuovi_messaggio(obj, self.lista_messaggi)
        self.scriviLista()

    def getAttributi(self, id):
        return self.objMetodi.getAttributi(id, self.lista_messaggi)

    def getObject_message(self, id):
       return self.objMetodi.getObject_message(id, self.lista_messaggi)

    def get_lista(self):
        return self.objMetodi.get_lista(self.lista_messaggi)

    def notificaTurno(self, mittente, destinatario, messaggio, data):
        notifica = Messaggio(mittente, destinatario, messaggio, data)
        notifica.addToList(notifica)
