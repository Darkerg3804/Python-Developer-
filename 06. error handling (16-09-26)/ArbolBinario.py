class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None


class BSTUsuarios:
    def __init__(self):
        self.raiz = None

    # ---------- INSERTAR ----------
    def insertar(self, id, nombre):
        if self.raiz is None:
            self.raiz = Nodo(id, nombre)
        else:
            self._insertar(self.raiz, id, nombre)

    def _insertar(self, nodo, id, nombre):
        if id < nodo.id:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(id, nombre)
            else:
                self._insertar(nodo.izquierda, id, nombre)
        elif id > nodo.id:
            if nodo.derecha is None:
                nodo.derecha = Nodo(id, nombre)
            else:
                self._insertar(nodo.derecha, id, nombre)
        else:
            # ID ya existe: actualizamos el nombre
            nodo.nombre = nombre

    # ---------- BUSCAR ----------
    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if nodo is None:
            return None
        if id == nodo.id:
            return nodo.nombre
        if id < nodo.id:
            return self._buscar(nodo.izquierda, id)
        return self._buscar(nodo.derecha, id)

    # ---------- RANGO ----------
    def rango(self, minimo, maximo):
        resultado = []
        self._rango(self.raiz, minimo, maximo, resultado)
        return resultado

    def _rango(self, nodo, minimo, maximo, resultado):
        if nodo is None:
            return
        # Si el nodo es mayor que el mínimo, puede haber algo a la izquierda
        if nodo.id > minimo:
            self._rango(nodo.izquierda, minimo, maximo, resultado)
        # Si el nodo está en el rango, lo agregamos
        if minimo <= nodo.id <= maximo:
            resultado.append((nodo.id, nodo.nombre))
        # Si el nodo es menor que el máximo, puede haber algo a la derecha
        if nodo.id < maximo:
            self._rango(nodo.derecha, minimo, maximo, resultado)

    # ---------- MÍNIMO Y MÁXIMO ----------
    def minimo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.izquierda:
            nodo = nodo.izquierda
        return (nodo.id, nodo.nombre)

    def maximo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.derecha:
            nodo = nodo.derecha
        return (nodo.id, nodo.nombre)

    # ---------- RECORRIDO IN-ORDER ----------
    def in_order(self):
        resultado = []
        self._in_order(self.raiz, resultado)
        return resultado

    def _in_order(self, nodo, resultado):
        if nodo:
            self._in_order(nodo.izquierda, resultado)
            resultado.append((nodo.id, nodo.nombre))
            self._in_order(nodo.derecha, resultado)