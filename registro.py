class Atencion:
    def __init__(self, nombre, dni, codigo_paciente, especialidad, codigo_medico):
        self._nombre = nombre
        self._dni = dni
        self._codigo_paciente = codigo_paciente
        self._especialidad = especialidad
        self._codigo_medico = codigo_medico

    @property
    def nombre(self):
        return self._nombre
    @property
    def dni(self):
        return self._dni
    @property
    def codigo_paciente(self):
        return self._codigo_paciente
    @property
    def especialidad(self):
        return self._especialidad
    @property
    def codigo_medico(self):
        return self._codigo_medico
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @dni.setter
    def dni(self, valor):
        self._dni = valor
    @codigo_paciente.setter
    def codigo_paciente(self, valor):
        self._codigo_paciente = valor
    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor
    @codigo_medico.setter
    def codigo_medico(self, valor):
        self._codigo_medico = valor

    def resumen(self):
        return f"{self._nombre} - {self._dni} - {self._codigo_paciente} - {self._especialidad} - {self._codigo_medico}"
    