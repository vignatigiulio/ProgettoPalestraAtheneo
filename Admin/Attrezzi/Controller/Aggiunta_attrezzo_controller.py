from Admin.Attrezzi.Model.Attrezzo import Attrezzo


class metodi_aggiungi_attrezzo(object):

    def salva(self, descrizione, data_acquisto, quantita, prezzo, data_manutenzione):
        objAttrezzo = Attrezzo(descrizione, data_acquisto, quantita, prezzo, data_manutenzione)
        objAttrezzo.addToList(objAttrezzo)
        objAttrezzo.scriviLista()
