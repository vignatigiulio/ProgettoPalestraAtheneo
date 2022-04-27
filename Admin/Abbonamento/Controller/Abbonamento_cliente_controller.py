from Admin.Abbonamento.Model.Abbonamento import Abbonamento


class metodi_abbonamento_cliente(object):
    objAbbonamento = Abbonamento()

    def creaOggettoAbbonamento(self, tipo_abbonamento, data_iscrizione, data_certificato_medico):
        scheda_Abbonamento = Abbonamento(data_iscrizione, data_certificato_medico, tipo_abbonamento)
        self.objAbbonamento.addToList(scheda_Abbonamento)