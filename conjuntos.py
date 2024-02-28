import matplotlib
import sys
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import tkinter as tk
from tkinter import simpledialog, messagebox


def union_conjuntos(conjunto_a, conjunto_b):
    conjunto_union = set()

    for i in conjunto_a:
        if i not in conjunto_union:
            conjunto_union.add(i)

    for i in conjunto_b:
        if i not in conjunto_union:
            conjunto_union.add(i)

    return conjunto_union


def interseccion(conjunto_a, conjunto_b):
    conjunto_interseccion = set()

    for i in conjunto_a:
        if i in conjunto_b:
            conjunto_interseccion.add(i)

    return conjunto_interseccion


def diferencia(conjunto_a, conjunto_b):
    conjunto_diferencia = set()

    for i in conjunto_a:
        if i not in conjunto_b:
            conjunto_diferencia.add(i)

    return conjunto_diferencia


def complemento(conjunto_u, conjunto_a):
    return diferencia(conjunto_u, conjunto_a)


def cardinalidad(conjunto_a):
    return len(conjunto_a)


def es_subconjunto(a, b):
    for elemento in a:
        if elemento not in b:
            return False
    return True


def son_disjuntos(conjunto_a, conjunto_b):
    intersecc = interseccion(conjunto_a, conjunto_b)
    return len(intersecc) == 0


def diagramar(diagrama):
    for i in lista_conjuntos:
        diagrama


def recibir_conjunto(numero_conjunto):
    entrada = simpledialog.askstring("Ingresar conjunto", f"Ingrese los elementos del conjunto {numero_conjunto} separados por comas: ")
    elementos = entrada.split(',')  # Suponiendo que los elementos están separados por comas
    return set(elementos)


lista_conjuntos = list()


def ingreso_conjuntos(numero_conjuntos):
    if len(lista_conjuntos) > 0:
        messagebox.showinfo("Error", "Ya ingresó los conjuntos. No puede ingresar más")
        salir()

    for i in range(1, numero_conjuntos + 1):
        lista_conjuntos.append(recibir_conjunto(i))


def salir():
    messagebox.showinfo("Saliendo", "Saliendo del programa.")
    sys.exit()


def generar_diagrama2():
    set1 = lista_conjuntos[0]
    set2 = lista_conjuntos[1]

    # Calcular las intersecciones
    interseccion_set1_set2 = interseccion(set1, set2)
    diferencia_set1_set2 = diferencia(set1, set2)
    diferencia_set2_set1 = diferencia(set2, set1)

    # Crear el diagrama de Venn
    venn = venn2([set1, set2], ('Conjunto 1', 'Conjunto 2'))

    # Mostrar los elementos de la intersección y los que no están en la intersección
    if venn.get_label_by_id('10') is not None:
        venn.get_label_by_id('10').set_text('\n'.join(sorted(interseccion_set1_set2)))
    if venn.get_label_by_id('01') is not None:
        venn.get_label_by_id('01').set_text('\n'.join(sorted(diferencia_set2_set1)))
    if venn.get_label_by_id('11') is not None:
        venn.get_label_by_id('11').set_text('\n'.join(sorted(diferencia_set1_set2)))

    # Ajustar el espaciado de las etiquetas
    for text in venn.set_labels:
        text.set_fontsize(11)  # Tamaño de fuente
        text.set_fontweight('bold')  # Negrita
        text.set_color('black')  # Color del texto

    plt.show()


def generar_diagrama3():
    set1 = lista_conjuntos[0]
    set2 = lista_conjuntos[1]
    set3 = lista_conjuntos[2]

    # Calcular las intersecciones
    intersecciones = {
        '100': set1 - set2 - set3,
        '010': set2 - set1 - set3,
        '001': set3 - set1 - set2,
        '110': set1 & set2 - set3,
        '101': set1 & set3 - set2,
        '011': set2 & set3 - set1,
        '111': set1 & set2 & set3
    }

    # Crear el diagrama de Venn
    venn = venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set1 & set2 - set3),
                          len(set3 - set1 - set2), len(set1 & set3 - set2), len(set2 & set3 - set1),
                          len(set1 & set2 & set3)),
                 set_labels=('Conjunto 1', 'Conjunto 2', 'Conjunto 3'))

    # Mostrar los elementos de cada conjunto sin comas
    for subset, conjunto in intersecciones.items():
        if venn.get_label_by_id(subset) is not None:
            venn.get_label_by_id(subset).set_text(
                '\n'.join(sorted(conjunto)))  # Usamos '\n' para separar los elementos en líneas

    # Ajustar el espaciado de las etiquetas
    for text in venn.set_labels:
        text.set_fontsize(11)  # Tamaño de fuente
        text.set_fontweight('bold')  # Negrita
        text.set_color('black')  # Color del texto

    plt.show()


def union_menu():
    union_con = set()
    if len(lista_conjuntos) == 2:
        union_con = union_conjuntos(lista_conjuntos[0], lista_conjuntos[1])
    else:
        temp_con = union_conjuntos(lista_conjuntos[0], lista_conjuntos[1])
        union_con = union_conjuntos(temp_con, lista_conjuntos[2])
    return union_con


def interseccion_menu():
    inter_con = set()
    if len(lista_conjuntos) == 2:
        inter_con = interseccion(lista_conjuntos[0], lista_conjuntos[1])
    else:
        temp_con = interseccion(lista_conjuntos[0], lista_conjuntos[1])
        inter_con = interseccion(temp_con, lista_conjuntos[2])
    return inter_con


def diferencia_menu():
    if len(lista_conjuntos) == 2:
        set1 = diferencia(lista_conjuntos[0], lista_conjuntos[1])
        set2 = diferencia(lista_conjuntos[1], lista_conjuntos[0])
        messagebox.showinfo("Diferencia de conjuntos", f"Conjunto 1 - Conjunto 2: {set1}\nConjunto 2 - Conjunto 1: {set2}")
    else:
        set1 = diferencia(lista_conjuntos[0], lista_conjuntos[1])
        set2 = diferencia(lista_conjuntos[0], lista_conjuntos[2])
        set3 = diferencia(lista_conjuntos[1], lista_conjuntos[0])
        set4 = diferencia(lista_conjuntos[1], lista_conjuntos[2])
        set5 = diferencia(lista_conjuntos[2], lista_conjuntos[0])
        set6 = diferencia(lista_conjuntos[2], lista_conjuntos[1])

        messagebox.showinfo("Diferencia de conjuntos", f"Conjunto 1 - Conjunto 2: {set1}\nConjunto 1 - Conjunto 3: {set2}\nConjunto 2 - Conjunto 1: {set3}\nConjunto 2 - Conjunto 3: {set4}\nConjunto 3 - Conjunto 2: {set5}\nConjunto 3 - Conjunto 1: {set6}")


def complemento_menu():
    if len(lista_conjuntos) == 2:
        conjunto_u = union_conjuntos(lista_conjuntos[0], lista_conjuntos[1])
        set1 = complemento(conjunto_u, lista_conjuntos[0])
        set2 = complemento(conjunto_u, lista_conjuntos[1])
        messagebox.showinfo("Complemento de conjuntos", f"C1^(∁): {set1}\nC2^(∁): {set2}")
    else:
        temp_con = union_conjuntos(lista_conjuntos[0], lista_conjuntos[1])
        conjunto_u = union_conjuntos(temp_con, lista_conjuntos[2])
        set1 = complemento(conjunto_u, lista_conjuntos[0])
        set2 = complemento(conjunto_u, lista_conjuntos[1])
        set3 = complemento(conjunto_u, lista_conjuntos[2])
        messagebox.showinfo("Complemento de conjuntos", f"Conjunto1^∁: {set1}\nConjunto2^∁: {set2}\nConjunto3^∁: {set3}")


def cardinalidad_menu():
    cardinalidades = ""
    for i in range(len(lista_conjuntos)):
        cardinalidades += f"Cardinalidad conjunto {i+1}: {cardinalidad(lista_conjuntos[i])}\n"
    messagebox.showinfo("Cardinalidad de conjuntos", cardinalidades)


def subconjunto_menu():
    # Verificar subconjuntos
    subconjuntos = ""
    if len(lista_conjuntos) == 2:
        set1 = lista_conjuntos[0]
        set2 = lista_conjuntos[1]

        es_subconjunto_1_2 = set1.issubset(set2)
        es_subconjunto_2_1 = set2.issubset(set1)
        subconjuntos += f"¿set1 es subconjunto de set2?: {es_subconjunto_1_2}\n"
        subconjuntos += f"¿set2 es subconjunto de set1?: {es_subconjunto_2_1}\n"
    else:
        set1 = lista_conjuntos[0]
        set2 = lista_conjuntos[1]
        set3 = lista_conjuntos[2]
        es_subconjunto_1_2 = es_subconjunto(set1, set2)
        es_subconjunto_1_3 = es_subconjunto(set1, set3)
        es_subconjunto_2_1 = es_subconjunto(set2, set1)
        es_subconjunto_2_3 = es_subconjunto(set2, set3)
        es_subconjunto_3_1 = es_subconjunto(set3, set1)
        es_subconjunto_3_2 = es_subconjunto(set3, set2)
        subconjuntos += f"¿set1 es subconjunto de set2?: {es_subconjunto_1_2}\n"
        subconjuntos += f"¿set1 es subconjunto de set3?: {es_subconjunto_1_3}\n"
        subconjuntos += f"¿set2 es subconjunto de set1?: {es_subconjunto_2_1}\n"
        subconjuntos += f"¿set2 es subconjunto de set3?: {es_subconjunto_2_3}\n"
        subconjuntos += f"¿set3 es subconjunto de set1?: {es_subconjunto_3_1}\n"
        subconjuntos += f"¿set3 es subconjunto de set2?: {es_subconjunto_3_2}\n"
    messagebox.showinfo("Verificar subconjuntos", subconjuntos)


def disjunto_menu():
    # Verificar disjuntos
    disjuntos = ""
    if len(lista_conjuntos) == 2:
        set1 = lista_conjuntos[0]
        set2 = lista_conjuntos[1]

        es_disjunto_1_2 = son_disjuntos(set1, set2)
        es_disjunto_2_1 = son_disjuntos(set2, set1)
        disjuntos += f"¿set1 es disjunto de set2?: {es_disjunto_1_2}\n"
        disjuntos += f"¿set2 es disjunto de set1?: {es_disjunto_2_1}\n"
    else:
        set1 = lista_conjuntos[0]
        set2 = lista_conjuntos[1]
        set3 = lista_conjuntos[2]
        es_disjunto_1_2 = son_disjuntos(set1, set2)
        es_disjunto_1_3 = son_disjuntos(set1, set3)
        es_disjunto_2_1 = son_disjuntos(set2, set1)
        es_disjunto_2_3 = son_disjuntos(set2, set3)
        es_disjunto_3_1 = son_disjuntos(set3, set1)
        es_disjunto_3_2 = son_disjuntos(set3, set2)
        disjuntos += f"¿set1 es disjunto de set2?: {es_disjunto_1_2}\n"
        disjuntos += f"¿set1 es disjunto de set3?: {es_disjunto_1_3}\n"
        disjuntos += f"¿set2 es disjunto de set1?: {es_disjunto_2_1}\n"
        disjuntos += f"¿set2 es disjunto de set3?: {es_disjunto_2_3}\n"
        disjuntos += f"¿set3 es disjunto de set1?: {es_disjunto_3_1}\n"
        disjuntos += f"¿set3 es disjunto de set2?: {es_disjunto_3_2}\n"
    messagebox.showinfo("Verificar disjuntos", disjuntos)


def menu():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    options = [
        "Ingresar los conjuntos",
        "Generar diagrama de Venn de los conjuntos",
        "Unión de conjuntos",
        "Intersección de conjuntos",
        "Diferencia de conjuntos",
        "Complemento de un conjunto",
        "Cardinalidad de un conjunto",
        "Verificar si un conjunto es subconjunto de otro",
        "Verificar si dos conjuntos son disjuntos",
        "Salir"
    ]
    choice = simpledialog.askinteger("Menú", "Elige una opción:\n0. Ingresar los conjuntos\n1. Generar diagrama de Venn de los conjuntos\n2. Unión de conjuntos\n3. Intersección de conjuntos\n4. Diferencia de conjuntos\n5. Complemento de un conjunto\n6. Cardinalidad de un conjunto\n7. Verificar si un conjunto es subconjunto de otro\n8. Verificar si dos conjuntos son disjuntos\n9. Salir", minvalue=0, maxvalue=9)

    return choice


def ejecutar_opcion(opcion):
    if opcion is None:
        salir()
    else:
        if opcion == 0:
            num_con = simpledialog.askinteger("Número de conjuntos", "Ingrese el número de conjuntos que va a utilizar. 2 o 3.", minvalue=2, maxvalue=3)
            ingreso_conjuntos(num_con)
        elif opcion == 1:
            if len(lista_conjuntos) == 2:
                generar_diagrama2()
            else:
                generar_diagrama3()
        elif opcion == 2:
            messagebox.showinfo("Unión de conjuntos", str(union_menu()))
        elif opcion == 3:
            messagebox.showinfo("Intersección de conjuntos", str(interseccion_menu()))
        elif opcion == 4:
            diferencia_menu()
        elif opcion == 5:
            complemento_menu()
        elif opcion == 6:
            cardinalidad_menu()
        elif opcion == 7:
            subconjunto_menu()
        elif opcion == 8:
            disjunto_menu()
        elif opcion == 9:
            salir()


# Función principal
def main():
    while True:
        opcion = menu()
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
