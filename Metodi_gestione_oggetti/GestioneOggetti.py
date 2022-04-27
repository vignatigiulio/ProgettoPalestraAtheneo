import pickle
from PyQt5.QtWidgets import QMessageBox
import os
from os import listdir
from os.path import isfile, join


class GestioneOggetti(object):

    @staticmethod
    def popolaLista(lista):
        if len(lista) > 0:
            f = []
            for x in lista:
                f.append(x.nome + " " + x.cognome)
            return f

    @staticmethod
    def recuperaSalvataggio(path, lista):
        if os.path.exists(path) and os.path.getsize(path) != 0:
            with(open(path, "rb")) as openfile:
                while True:
                    try:
                        lista.append(pickle.load(openfile))
                    except EOFError:
                        break

    @staticmethod
    def addToList(obj, lista):
        lista.append(obj)

    @staticmethod
    def rimuovi(strdaeliminare, lista):
        for x in lista:
            if x.nome + " " + x.cognome == strdaeliminare:
                lista.remove(x)
                return

    @staticmethod
    def scriviLista(path, lista):
        filehandler = open(path, 'wb')
        for x in lista:
            pickle.dump(x, filehandler)

    @staticmethod
    def getAttributi(id, lista):
        for x in lista:
            if x.nome + " " + x.cognome == id:
                return x

    @staticmethod
    def getObject(id, lista):
        for x in lista:
            if x.nome + x.cognome == id:
                return x

    @staticmethod
    def getObject_message(id, lista):
        lista_nuova = []
        for x in lista:
            if x.destinatario == id or x.mittente == id:
                lista_nuova.append(x)
        return lista_nuova

    @staticmethod
    def getUserPass(list):
        credenziali = dict()
        for dati in list:
            credenziali[dati.nome + dati.cognome] = dati.password
        return credenziali

    @staticmethod
    def resetpassword(name, lista):
        for x in lista:
            if x.nome + " " + x.cognome == name:
                x.password = "1234"
                return

    @staticmethod
    def popolaListaAttrezzi(listaAtt):
        if len(listaAtt) > 0:
            f = []
            for x in listaAtt:
                f.append(x)
            return f

    @staticmethod
    def addToListAtt(obj, lista):
        lista.append([obj.descr, obj.data_ac, obj.quantita, obj.pr_uni, obj.data_man])

    @staticmethod
    def rimuoviAttrezzo(riga, lista):
        lista.remove(lista[riga])

    @staticmethod
    def get_lista(lista):
        vett = []
        for elem in lista:
            vett.append(elem.nome + elem.cognome)
        return vett

    @staticmethod
    def rimuovi_messaggio(obj, lista):
        for x in lista:
            if x.mittente == obj.mittente and x.destinatario == obj.destinatario and x.contenuto == obj.contenuto and \
                    x.data == obj.data:
                lista.remove(x)
                break



    @staticmethod
    def rimuoviFiles(percorso):
        os.remove(percorso)


    @staticmethod
    def controlloGiorno(data, lista_turni):
        lista_prenotati = []
        for elem in lista_turni:
            if data == elem.data:
                lista_prenotati.append(elem)
        return lista_prenotati

    def controlloLavoro(self, data, staff, lista_turni):
        lista_lavori = []
        for elem in lista_turni:
            if data == elem.data and staff == self.getIndirizzo(elem.staff):
                lista_lavori.append(elem)
        return lista_lavori

    @staticmethod
    def getIndirizzo(username):
        indirizzo = ""
        str = username.split(" ")
        for elem in str:
            indirizzo += elem
        return indirizzo

    def rimuoviTurno(self, username, data, tipo, orario, lista_turni, percorso):
        for elem in lista_turni:
            if elem.data == data and elem.staff == username and elem.tipo == tipo and elem.orario == orario:
                lista_turni.remove(elem)
        self.scriviLista(percorso, lista_turni)

    def confrontaTurno(self, oggetto, lista):
        for elem in lista:
            if oggetto.staff == elem.staff and oggetto.data == elem.data and \
                    oggetto.tipo == elem.tipo and elem.orario == oggetto.orario:
                return True
        return False

    @staticmethod
    def rimuoviTurniStaff(username, percorso, lista_turni):
        filehandler = open(percorso, 'wb')
        for elem in lista_turni:
            if elem.staff != username:
                pickle.dump(elem, filehandler)

    def show_popup_ok(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    def show_popup_exception(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    @staticmethod
    def getListaFiles(percorso):
        listafiles = [f for f in listdir(percorso) if isfile(join(percorso, f))]
        return listafiles

    def show_popup_question(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.No)
        risposta = self.msg.exec_()
        if risposta == QMessageBox.Yes:
            return True
        elif risposta == QMessageBox.No:
            return False
