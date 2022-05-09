from Metodi_gestione_oggetti.GestioneOggetti import GestioneOggetti
from Admin.Cliente.Model.Cliente import Cliente
from Admin.Staff.Model.Staff import Staff


class metodi_cambio_password(object):
    objMetodi = GestioneOggetti()
    caratteri_minimi = 7
    caratteri_massimi = 17

    def impostaPassword(self, tipo, password1, password2, username):
        try:
            if tipo == "Cliente":
                objCliente = Cliente()
                objCliente = objCliente.getObject(username)
                if password1 == password2:
                    if self.caratteri_minimi < len(password1) < self.caratteri_massimi:
                        objCliente.password = password1
                        objCliente.scriviLista()
                        return 0
                    else:
                        return -1
                else:
                    return -2
            else:
                objStaff = Staff()
                objStaff = objStaff.getObject(username)
                if password1 == password2:
                    if self.caratteri_minimi < len(password1) < self.caratteri_massimi:
                        objStaff.password = password1
                        objStaff.scriviLista()
                        return 0
                    else:
                        return -1
                else:
                    return -2
        except Exception:
            return -3
