def main():
    def analysis(numeros, palabras):
        numlen = [len(i) for i in numeros]
        strlen = [len(i) for i in palabras]
        print('Tamano numeros: ' + ','.join(map(str,numlen)))
        print('Tamano palabras: ' + ','.join(map(str,strlen)))
        numlen = [i for i in numlen if i != max(numlen)]
        strlen = [i for i in strlen if i != max(strlen)]
        return numlen + strlen

    numeros = []
    palabras = []
    for i in range(5):
        numeros.append(input('Ingrese valor para lista numeros: '))
    for i in range(5):
        palabras.append(input('Ingrese valor para lista palabras: '))

    print("Numeros: " + ','.join(numeros))
    print("Palabras: " + ','.join(palabras))
    final = analysis(numeros, palabras)
    print("Lista tamano: " + ','.join(map(str,final)))
