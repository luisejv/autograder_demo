def main():
    import random

    def desordenar(lista):
        random.seed(None)
        for i in range(len(lista)):
            num = random.randint(0, len(lista)-1)
            aux = lista[i]
            lista[i] = lista[num]
            lista[num] = aux

    lista = []
    for i in range(10):
        lista.append(int(input("Ingrese valor para la lista: ")))
    listaStr = "" + str(lista[0])
    for i in range(1, len(lista)):
        listaStr += "," + str(lista[i])
    print("Lista: " + listaStr)
    desordenar(lista)
    listaStr = "" + str(lista[0])
    for i in range(1, len(lista)):
        listaStr += "," + str(lista[i])
    print("Lista desordenada: " + listaStr)