class Buscar_codigo:
    def __init__(self, codigo, objeto):
        self._codigo = codigo
        self._objeto = objeto

    @property
    def codigo(self):
        return self._codigo
    @property
    def objeto(self):
        return self._objeto
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
    @objeto.setter
    def objeto(self, valor):
        self._objeto = valor
    def buscar(self, codigo):
        if self._codigo == codigo:
            return self._objeto
        else:
            return None

    def resumen(self):
        return f"Codigo: {self._codigo}"
    