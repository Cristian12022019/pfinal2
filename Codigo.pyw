from tkinter import *
from random import sample

# Funciones de ordenamiento
def quicksort(vectorquick, start=0, end=None):
    # Código de ordenamiento QuickSort
    """
    Esta función ordenará el vector que le pases como argumento 
    con el Método Quick Sort
    """
    if end is None:
        end = len(vectorquick) - 1
        
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con quick es:", vectorquick)
    
    def quick(vectorquick, start, end):
        if start >= end:
            return

        def particion(vectorquick, start, end):
            pivot = vectorquick[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos 
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica 
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorquick[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior            
                while menor <= mayor and vectorquick[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]

            return mayor

        p = particion(vectorquick, start, end)
        quick(vectorquick, start, p-1)
        quick(vectorquick, p+1, end)

    quick(vectorquick, start, end)
    print("El vector ordenado con quick es:", vectorquick)
    pass
    
def shellsort(vectorshell):
    # Código de ordenamiento ShellSort
    """
    Esta función ordenará el vector que le pases como argumento 
    con el Método Shell Sort
    """
    print("El vector a ordenar con shell es:", vectorshell)

    largo = len(vectorshell)
    distancia = largo // 2

    # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2  # Acotamos la distancia nuevamente y continua el ciclo
    print("El vector ordenado con shell es: ", vectorshell)
    pass
    
# Crear una clase de interfaz gráfica
class SortingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Metodo de ordenamiento")

        # Crear etiquetas y campos de entrada
        self.label = Label(master, text="Ingrese los números separados por espacio:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        # Crear botones para ordenar
        self.quick_button = Button(master, text="Ordenar con QuickSort", command=self.quick_sort)
        self.quick_button.pack()

        self.shell_button = Button(master, text="Ordenar con ShellSort", command=self.shell_sort)
        self.shell_button.pack()

        # Crear etiquetas para mostrar los vectores antes y después de ser ordenados
        self.original_vector_label = Label(master, text="Vector original:")
        self.original_vector_label.pack()

        self.sorted_vector_label = Label(master, text="Vector ordenado:")
        self.sorted_vector_label.pack()

    def quick_sort(self):
        # Obtener los números ingresados por el usuario y ordenar con QuickSort
        numeros = self.entry.get()
        vectorquick = list(map(int, numeros.split()))
        self.original_vector_label.config(text=f"Vector original: {vectorquick}")
        quicksort(vectorquick)
        self.sorted_vector_label.config(text=f"Vector ordenado: {vectorquick}")

    def shell_sort(self):
        # Obtener los números ingresados por el usuario y ordenar con ShellSort
        numeros = self.entry.get()
        vectorshell = list(map(int, numeros.split()))
        self.original_vector_label.config(text=f"Vector original: {vectorshell}")
        shellsort(vectorshell)
        self.sorted_vector_label.config(text=f"Vector ordenado: {vectorshell}")

# Crear la ventana principal y ejecutar la interfaz gráfica
root = Tk()
my_gui = SortingGUI(root)
root.mainloop()
