# Parcial 2 - Estructura de Datos I
# Código base final
# ============================================================


# ============================================================
# Punto 1: Lista Circular - Josephus modificado
# ============================================================

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(n, m):
        head= Node(1)
        cur=head
        for i in range(2,n+1):
            cur.next= Node(i)
            cur=cur.next
        cur.next=head
        cur=head
        while cur.next is not cur:
            for _ in range(m-2):
                cur=cur.next
                to_del=cur.next
                cur.next=to_del.next
        if to_del.val % 5==0:
            cur.next=cur.next.next
        
        return cur.val
        
        pass


# ============================================================
# Punto 2: Lista Simple - Método único
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
        slow=head
        fast=head 
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            second.next,prev,second=prev,second,second.next
        
        return head,prev




# ============================================================
# Pruebas base
# ============================================================

if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    print("\n===== Punto 2 =====")
    lista_s = ListaSimple()

    for x in [1, 2, 3, 4, 5, 6]:
        lista_s.insertar_final(x)

    lista_s.mostrar()

    lista_s.partir_voltear_intercalar()

    print("Resultado:")
    lista_s.mostrar()