class Progama_cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def codigo(self):
        return self._codigo
    @property
    def paciente(self):
        return self._paciente
    @property
    def medico(self):
        return self._medico
    @property
    def fecha(self):
        return self._fecha
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor
    @medico.setter
    def medico(self, valor):
        self._medico = valor
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def resumen(self):
        return f"{self._codigo} - {self._paciente} - {self._medico} - {self._fecha}"