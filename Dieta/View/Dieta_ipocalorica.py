from PyQt5 import QtCore, QtGui, QtWidgets


class dieta_ipocalorica(object):

    def setupUi(self, Form):
        self.finestra = Form
        Form.setObjectName("Form")
        Form.resize(536, 596)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(0, 30, 531, 511))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 531, 375))
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 531, 381))
        self.label_2.setObjectName("label_2")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 531, 375))
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 531, 381))
        self.label_3.setObjectName("label_3")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 521, 381))
        self.label_4.setObjectName("label_4")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 531, 381))
        self.label_5.setObjectName("label_5")
        self.toolBox.addItem(self.page_4, "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 121, 16))
        self.label.setObjectName("label")
        self.btnIndietro = QtWidgets.QPushButton(Form)
        self.btnIndietro.setGeometry(QtCore.QRect(350, 550, 113, 32))
        self.btnIndietro.setObjectName("btnIndietro")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnIndietro.clicked.connect(self.finestra.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dieta ipocalorica"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>La dieta ipocalorica è un regime alimentare "
                                                "che prevede un apporto <br/>calorico/energetico quotidiano inferiore "
                                                "a quello richiesto dall\'organismo<br/>nell\'arco della "
                                                "giornata.</p><p>All\'occhio di un professionista, tale definizione "
                                                "potrebbe sembrare riduttiva<br/>o solo parzialmente condivisibile; "
                                                "in effetti, le caratteristiche e i requisiti di<br/>una buona dieta "
                                                "ipocalorica sono molto più numerosi, ma, in senso stretto, "
                                                "<br/>l\'etimologia del termine è a dir poco essenziale, "
                                                "ovvero:</p><p>-<span style=\" font-weight:600;\">Dieta:</span> "
                                                "regole di alimentazione o regime alimentare controllato, "
                                                "frutto di <br/>un\'indicazione terapeutica; dal greco "
                                                "&quot;dìaita&quot; che significa &quot;stile di "
                                                "vita&quot;.<br/>-<span style=\" font-weight:600;\">ipo-</span>: "
                                                "particella diminutiva.<br/>-<span style=\" "
                                                "font-weight:600;\">calorica:</span> che ha o apporta "
                                                "calorie/energia.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Cos\'è?"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DEVE "
                                                "</span>essere prescritta/valutata/strutturata e seguita da un "
                                                "professionista </p><p>qualificato (dietologo, biologo specializzato "
                                                "in nutrizione o dietista).</p><p><br/></p><p><span style=\" "
                                                "font-weight:600;\">DEVE</span> essere utilizzata <span style=\" "
                                                "font-weight:600;\">SOLO</span> in caso di necessità; come se fosse "
                                                "un </p><p>&quot;ciclo farmacologico&quot;, la dieta ipocalorica NON "
                                                "giova alle persone sane</p><p> in normopeso e/o senza alterazioni "
                                                "del metabolismo che la rendano giustificabile.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Prescrizione"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>L\'utilizzo &quot;primario&quot; di questa "
                                                "dieta è finalizzato al dimagrimento, </p><p>ovvero alla riduzione "
                                                "della massa grassa e della circonferenza addominale,</p><p>quindi "
                                                "dell\'indice di massa corporea/body mass index (IMC/BMI). </p><p>E\' "
                                                "ben noto quanto il sovrappeso e ancor peggio l\'obesità siano "
                                                "correlati </p><p>all\'insorgenza di malattie metaboliche, "
                                                "primarie e secondarie, di natura </p><p>ambientale e/o ereditaria; "
                                                "alcuni esempi sono:</p><p>-<span style=\" "
                                                "font-weight:600;\">dislipidemie</span> (colesterolo TOT e/o LDL "
                                                "alto, trigliceridi alti, entrambi).</p><p>-<span style=\" "
                                                "font-weight:600;\">ipertensione arteriosa</span>.</p><p>-<span "
                                                "style=\" font-weight:600;\">iperuricemia</span> e/o <span style=\" "
                                                "font-weight:600;\">gotta</span>.</p><p>- <span style=\" "
                                                "font-weight:600;\">iperglicemia</span> o<span style=\" "
                                                "font-weight:600;\"> diabete mellito tipo "
                                                "2</span>.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Quando usarla"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>Il rispetto della dieta ipocalorica è sempre "
                                                "il risultato di una formula</p><p> astratta <span style=\" "
                                                "font-weight:600;\">NON</span> matematicamente valutabile, "
                                                "le cui variabili sono:<br/><br/>-Rapporto paziente-operatore ("
                                                "fiducia, onestà, empatia, capacità di </p><p>dialogo, capacità di "
                                                "ascolto e comprensione, comunicatività, intuito,</p><p> astuzia, "
                                                "capacità di indurre motivazione ecc.)</p><p><br/>-Accuratezza e "
                                                "precisione del "
                                                "metodo.</p><p><br/>-Personalizzazione.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Come Strutturarla"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Dieta "
                                              "Ipocalorica</span></p></body></html>"))
        self.btnIndietro.setText(_translate("Form", "Indietro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dieta_ipocalorica()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
