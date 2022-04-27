from Cliente.Allenamenti.Model.Allenamento import lista_esercizi

class metodi_esercizi(object):
    Model = lista_esercizi()

    def creaOggetto(self, username, esercizi):
        objAllenamento = lista_esercizi(username, esercizi)
        self.Model.aggiungiAllaLista(objAllenamento)


