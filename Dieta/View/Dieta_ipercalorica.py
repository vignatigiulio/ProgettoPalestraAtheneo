from PyQt5 import QtCore, QtGui, QtWidgets


class dieta_ipercalorica(object):

    def setupUi(self, Form):
        self.finestra = Form
        Form.setObjectName("Form")
        Form.resize(526, 586)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(0, 30, 511, 501))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 511, 365))
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 511, 381))
        self.label_2.setObjectName("label_2")
        self.toolBox.addItem(self.page, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 511, 381))
        self.label_3.setObjectName("label_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 511, 365))
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 511, 381))
        self.label_4.setObjectName("label_4")
        self.toolBox.addItem(self.page_2, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 521, 371))
        self.label_5.setObjectName("label_5")
        self.toolBox.addItem(self.page_4, "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 121, 16))
        self.label.setObjectName("label")
        self.btnIndietro = QtWidgets.QPushButton(Form)
        self.btnIndietro.setGeometry(QtCore.QRect(360, 540, 113, 32))
        self.btnIndietro.setObjectName("btnIndietro")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnIndietro.clicked.connect(self.finestra.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dieta ipercalorica"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>La dieta ipercalorica è un regime alimentare "
                                                "utile a fornire più energia,</p><p>nutrienti e acqua rispetto al "
                                                "regime alimentare per il mantenimento</p><p>del peso; viene "
                                                "utilizzata nel ripristino del peso (INCREMENTO</p><p>ponderale) dei "
                                                "soggetti valutati in sottopeso (ovvero con </p><p>un indice di massa "
                                                "corporea &lt;18,5 punti), e/o malnutriti.</p><p>In alcuni casi, "
                                                "la dieta ipercalorica può rappresentare un valido sostegno "
                                                "</p><p>per gli allenamenti di ginnastica pesante incentrati sullo "
                                                "sviluppo della </p><p>massa muscolare (aumento della sezione "
                                                "trasversa dei fasci), </p><p>purché rispettino i principi "
                                                "fondamentali della dietetica.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Cos\'è?"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>-Equilibrio nutrizionale dei macronutrienti "
                                                "energetici: 25% lipidi, </p><p>0,75-1,5g/kg di peso fisiologico "
                                                "desiderabile di proteine, </p><p>il resto dell\'energia sotto forma "
                                                "di glucidi.</p><p><br/>-Garanzia dei nutrienti essenziali, "
                                                "delle vitamine e dei sali minerali </p><p>(è sufficiente attenersi "
                                                "alle linee guida di una buona e sana "
                                                "alimentazione)</p><p><br/></p><p>-Surplus energetico MASSIMO del 10% "
                                                "rispetto alla normo-calorica.</p><p><br/></p><p>-Contenimento dei "
                                                "nutrienti potenzialmente nocivi se in eccesso: </p><p>colesterolo, "
                                                "saccarosio aggiunto, cloruro di sodio (Na), </p><p>grassi saturi, "
                                                "in alcuni casi anche la fibra ecc.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Principi Fondamentali"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>A livello pratico, la dieta ipercalorica non è "
                                                "di difficile stesura; </p><p>è sufficiente svolgere l\'impostazione "
                                                "di una normo-calorica </p><p>+ 10% dell\'energia, "
                                                "adattare l\'apporto proteico in base alle</p><p> necessità (tra 0,"
                                                "75 e 1,5g/kg) e scegliere correttamente </p><p>gli alimenti per il "
                                                "raggiungimento di tutti i</p><p> fabbisogni raccomandati (ferro, "
                                                "calcio, tiamina, riboflavina, niacina, ecc).</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Indicazioni Pratiche"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>Non ci sono cibi specifici, l’importante resta "
                                                "l’assicurarsi il bilancio energetico <br/>positivo. Anche se "
                                                "potrebbe essere facile pensare che debba essere un "
                                                "regime<br/>alimentare molto ricco di alimenti proteici, "
                                                "in realtà non deve necessariamente <br/>essere (come vedremo) una "
                                                "dieta iperproteica.</p><p>Mangiare di più significa che le quantità "
                                                "e/o la qualità dei tuoi pasti cambia: <br/>le porzioni di uno stesso "
                                                "alimento diventano più grandi oppure ti dirigi verso <br/>la scelta "
                                                "di alimenti più calorici a parità di quantità. <br/>Soprattutto se "
                                                "ti sazi facilmente, è consigliabile:</p><p>-<span style=\" "
                                                "font-weight:600;\">scegliere fonti densamente energetiche</span>: "
                                                "quelle che anche in piccole quantità <br/>apportano molta energia, "
                                                "come ad esempio olio e frutta secca.</p><p>-<span style=\" "
                                                "font-weight:600;\">scegliere cibi meno sazianti:</span> perciò "
                                                "limitare il consumo di prodotti fibrosi (cereali <br/>integrali, "
                                                "legumi) e/o acquosi (alimenti freschi come frutta, "
                                                "verdura).</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Cosa mangiare?"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Dieta "
                                              "Ipercalorica</span></p></body></html>"))
        self.btnIndietro.setText(_translate("Form", "Indietro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dieta_ipercalorica()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
