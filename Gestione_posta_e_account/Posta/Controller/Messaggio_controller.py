from Gestione_posta_e_account.Posta.Model.Messaggio import Messaggio
from Admin.Cliente.Model.Cliente import Cliente
from Admin.Staff.Model.Staff import Staff

class metodi_gestione_messaggi(object):
    Model = Messaggio()
    objCliente = Cliente()
    objStaff = Staff()

    def getListaClienti(self):
        return self.objCliente.get_lista()

    def getListaStaff(self):
        return self.objStaff.get_lista()

    def spedisciMessaggio(self, destinatario, username, testo, data):
        if testo.replace(" ", "") != "":
            messaggi = Messaggio(username, destinatario, testo, data)
            messaggi.addToList(messaggi)
            return True
        else:
            return False

    def selezioneDestinatario(self, chkClienti, chkStaff):
        if chkClienti or chkStaff:
            return True
        else:
            return False

    def recuperaSalvataggio(self):
        self.Model.recuperaSalvataggio()
