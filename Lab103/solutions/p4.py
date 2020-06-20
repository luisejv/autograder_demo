def main():
    import random

    def imprimirMatriz(matrix):
        for i in range(len(matrix)):
            linea = ' '.join(map(str, matrix[i]))
            print(linea)

    def changeMatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = '@' if (i + j) % 2 == 0 else '*'
        return matrix

    def contarAsteriscos(matrix):
        cont = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '*':
                    cont += 1
        return cont

    finished = False
    while not finished:
        n = int(input("Ingrese numero de filas: "))
        m = int(input("Ingrese numero de columnas: "))
        finished = n > 1 and m > 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(0, 10))
        matrix.append(row)
    print("Matriz original:")
    imprimirMatriz(matrix)
    newMatrix = changeMatrix(matrix)
    print("Matriz final:")
    imprimirMatriz(newMatrix)
    print('Suma asteriscos: ' + str(contarAsteriscos(newMatrix)))