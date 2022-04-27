import os
from os import listdir
from os.path import isfile, join
from PyQt5.QtWidgets import QFileDialog
from Admin.Cliente.Model.Cliente import Cliente
from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Dieta.Model.File_diete_cliente import File_diete_cliente

class metodi_dieta_cliente(object):
    objCliente = Cliente()
    objMetodi = GestioneOggetti()
    Model = File_diete_cliente()

    def salvaInfoCliente(self, username, altezza, peso, eta):
        self.objCliente = self.objCliente.getObject(username)
        self.objCliente.altezza = altezza
        self.objCliente.peso = peso
        self.objCliente.eta = eta

    def getSesso(self, username):
        return self.objCliente.getSesso(self.objCliente.getObject(username))

    def getEta(self, username):
        return self.objCliente.getEta(self.objCliente.getObject(username))

    def getPeso(self, username):
        return self.objCliente.getPeso(self.objCliente.getObject(username))

    def getAltezza(self, username):
        return self.objCliente.getAltezza(self.objCliente.getObject(username))

    def calcolaBMI(self, altezza, peso):
        bmi = peso / (altezza * altezza)
        return bmi

    def calcolaPeso(self, altezza, eta, sesso):
        coefficiente_peso_maschio = 100
        coefficiente_peso_femmina = 112
        weight = 0
        if sesso == "maschio":
            weight = 0.8 * (altezza * 100 - coefficiente_peso_maschio) + eta / 2
        elif sesso == "femmina":
            weight = 0.8 * (altezza * 100 - coefficiente_peso_femmina) + eta / 2
        return weight

    def calcoloADS(self, lavoro, attivita_fisica):
        if lavoro == "Lavori edile" or lavoro == "Lavori agricoli" or lavoro == "Operaio/a(pesante)":
            coefficiente_lavoro = 15
        else:
            coefficiente_lavoro = 10
        if attivita_fisica == "oltre 5 ore settimanali":
            coefficiente_attivita = 20
        elif attivita_fisica == "da 3 a 5 ore settimanali":
            coefficiente_attivita = 15
        else:
            coefficiente_attivita = 10
        coefficiente = coefficiente_attivita + coefficiente_lavoro
        return coefficiente

    def calcoloCalorie(self, sesso, peso, altezza, eta, lavoro, attivita_fisica):
        vettore_risposte = []
        if sesso == "maschio":
            MB = 66 + 13.7 * peso + 5 * altezza - 6.8 * eta
            fabbisogno_calorico = 1 * peso * 24
            fabbisogno_calorico += (fabbisogno_calorico * self.calcoloADS(lavoro, attivita_fisica)) / 100
            vettore_risposte.append(MB)
            vettore_risposte.append(fabbisogno_calorico)
            return vettore_risposte
        else:
            MB = 655 + 9.6 * peso + 1.8 * altezza - 4.7 * eta
            fabbisogno_calorico = 0.9 * peso * 24
            fabbisogno_calorico += (fabbisogno_calorico * self.calcoloADS(lavoro, attivita_fisica)) / 100
            vettore_risposte.append(MB)
            vettore_risposte.append(fabbisogno_calorico)
            return vettore_risposte

    def creaOggetto(self, username, bmi, peso_ideale, fabbisogno, segnalazioni):
        objDatiDieta = File_diete_cliente(username, bmi, peso_ideale, fabbisogno, segnalazioni)
        if self.Model.controllaRidondanza(username):
            self.Model.rimuoviOggetto(username)
        self.Model.aggiungiAllaLista(objDatiDieta)

    def popolaListaDiete(self):
        return self.Model.popolaListaDieta()

    def allegaFile(self):
        try:
            filename = QFileDialog.getOpenFileName()
            return filename[0]
        except(Exception):
            return

    def eliminaFileDietaVecchi(self, percorso, utente):
        lista_files = [f for f in listdir(percorso) if
                       isfile(join(percorso, f))]
        for elem in lista_files:
            if elem.startswith(utente):
                os.remove(percorso + elem)

    def getOggetto(self, username):
        return self.Model.getOggetto(username)