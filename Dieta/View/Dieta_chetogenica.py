from PyQt5 import QtCore, QtGui, QtWidgets


class dieta_chetogenica(object):

    def setupUi(self, Form):
        self.finestra = Form
        Form.setObjectName("Form")
        Form.resize(570, 602)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(10, 30, 551, 531))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 551, 283))
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_2.setObjectName("label_2")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 551, 261))
        self.label_3.setObjectName("label_3")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 60, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_5.setObjectName("label_5")
        self.toolBox.addItem(self.page_3, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_5.setObjectName("page_5")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_6.setObjectName("label_6")
        self.toolBox.addItem(self.page_5, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_4.setObjectName("page_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_7.setObjectName("label_7")
        self.toolBox.addItem(self.page_4, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 551, 283))
        self.page_6.setObjectName("page_6")
        self.label_8 = QtWidgets.QLabel(self.page_6)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_8.setObjectName("label_8")
        self.toolBox.addItem(self.page_6, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_7.setObjectName("page_7")
        self.label_9 = QtWidgets.QLabel(self.page_7)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label_9.setObjectName("label_9")
        self.toolBox.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 551, 293))
        self.page_8.setObjectName("page_8")
        self.label_10 = QtWidgets.QLabel(self.page_8)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 551, 291))
        self.label_10.setObjectName("label_10")
        self.toolBox.addItem(self.page_8, "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 121, 16))
        self.label.setObjectName("label")
        self.btnIndietro = QtWidgets.QPushButton(Form)
        self.btnIndietro.setGeometry(QtCore.QRect(460, 570, 93, 21))
        self.btnIndietro.setObjectName("btnIndietro")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnIndietro.clicked.connect(self.finestra.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dieta chetogenica"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>La dieta chetogenica è una strategia "
                                                "nutrizionalebasata sulla riduzione dei carboidrati</p><p> "
                                                "alimentari, che &quot;obbliga&quot; l\'organismo a produrre "
                                                "autonomamente il glucosio </p><p>necessario alla sopravvivenza e ad "
                                                "aumentare il consumo energetico dei grassi </p><p>contenuti nel "
                                                "tessuto adiposo. </p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Cos\'è?"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>La dieta chetogenica è uno schema "
                                                "nutrizionale:<br/><br/>-A basso contenuto di calorie (dieta "
                                                "ipocalorica).</p><p><br/>-A basso contenuto percentuale e assoluto "
                                                "di carboidrati (dieta low carb).</p><p><br/>-Ad alto contenuto "
                                                "percentuale di lipidi.</p><p><br/>-Ad alto contenuto percentuale di "
                                                "proteine.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Caratteristiche"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" "
                                                "font-weight:600;\">Consigliati:</span></p><p>-Carne, prodotti della "
                                                "pesca e uova – I gruppo fondamentale degli alimenti.</p><p>-Formaggi "
                                                "- II gruppo fondamentale degli alimenti.</p><p>-Grassi e oli da "
                                                "condimento – V gruppo fondamentale degli alimenti.</p><p>-Ortaggi – "
                                                "VI e VII gruppo fondamentale degli alimenti.</p><p><span style=\" "
                                                "font-weight:600;\">Sconsigliati:</span></p><p>-Cereali, "
                                                "patate e derivati – III gruppo fondamentale degli "
                                                "alimenti.</p><p>-Legumi – IV gruppo fondamentale degli "
                                                "alimenti.</p><p>-Frutti - VI e VII gruppo fondamentale degli "
                                                "alimenti.</p><p>-Bibite dolci, dolciumi vari, "
                                                "birra ecc.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Alimenti "))
        self.label_6.setText(_translate("Form", "<html><head/><body><p>Il meccanismo di funzionamento della dieta "
                                                "chetogenica si basa </p><p>sulla riduzione delle calorie e dei "
                                                "carboidrati alimentari che, </p><p>in associazione ad un giusto "
                                                "livello di proteine e un elevato</p><p> contenuto percentuale di "
                                                "grassi, dovrebbe migliorare la </p><p>lipolisi e l\'ossidazione "
                                                "lipidica cellulare, quindi il consumo totale</p><p> di grassi "
                                                "ottimizzando il dimagrimento. La produzione di corpi</p><p> "
                                                "chetonici, che dev\'essere assolutamente controllata, "
                                                "ha la </p><p>funzione di moderare lo stimolo </p><p>dell\'appetito – "
                                                "per il loro effetto anoressizzante.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Form", "Come funziona?"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>La produzione energetica cellulare avviene "
                                                "grazie alla </p><p>metabolizzazione di alcuni substrati, soprattutto "
                                                "glucosio</p><p> ed acidi grassi. Per lo più, questo processo inizia "
                                                "nel citoplasma </p><p>(glicolisi anaerobica – senza ossigeno) e "
                                                "termina nei </p><p>mitocondri (ciclo di Krebs – con ossigeno - e "
                                                "ricarica dell\'ATP).</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Metabolismo chetogenico"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Questa "
                                                "strategia alimentare viene utilizzata soprattutto in tre "
                                                "contesti:</span></p><p>-Dimagrimento (meglio se sotto controllo "
                                                "medico).</p><p>-Terapia alimentare di certe patologie metaboliche "
                                                "come l\'iperglicemia cronica, </p><p>l\'ipertrigliceridemia (solo "
                                                "sotto controllo medico), l\'ipertensione arteriosa e la "
                                                "</p><p>sindrome metabolica (mai in presenza di patologie o "
                                                "sofferenza di fegato e/o reni)</p><p>-Riduzione dei sintomi "
                                                "associati all\'epilessia infantile (esclusivamente quando "
                                                "il</p><p>soggetto non risponde alla terapia farmacologica e solo "
                                                "sotto controllo medico).</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("Form", "Utilizzi"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Facilita il "
                                                "dimagrimento grazie a:</span></p><p>-Riduzione delle calorie "
                                                "totali.</p><p>-Mantenimento di glicemia e insulinemia "
                                                "costanti.</p><p>-Aumento del consumo di grassi a scopo "
                                                "energetico.</p><p>-Incremento del dispendio calorico globale per "
                                                "aumento .</p><p>dell\'azione dinamico specifica e del &quot;lavoro "
                                                "metabolico&quot;.</p><p>-Ha un effetto "
                                                "anoressizzante.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("Form", "Vantaggi"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p>-Aumento della filtrazione renale e della "
                                                 "diuresi.</p><p>-Tendenza alla disidratazione.</p><p>-Aumento del "
                                                 "carico di lavoro dei reni.</p><p>-Possibile effetto tossico sui "
                                                 "reni da parte dei corpi chetonici.<br/>-Possibile ipoglicemia o "
                                                 "ipotensione.</p><p>-Mal di testa, affaticamento, vertigici, "
                                                 "nausea o irrtabilità.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), _translate("Form", "Svantaggi"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Dieta "
                                              "Chetogenica</span></p></body></html>"))
        self.btnIndietro.setText(_translate("Form", "Indietro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dieta_chetogenica()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())