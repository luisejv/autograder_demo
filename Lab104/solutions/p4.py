def main():
    import random

    def imprimirMatriz(matrix, n, m):
        for i in range(n):
            linea = ""
            for j in range(m):
                linea += str(matrix[i][j]) + " "
                #print(matrix[i][j], end=" ")
            print(linea)

    def changeMatrix(matrix):
        if len(matrix[0]) == len(matrix):
            for i in range(len(matrix)):
                if i % 2 != 0 :
                    for j in range(len(matrix[i])):
                        matrix[i][j] += 1
        else:
            for i in range(len(matrix)):
                if i % 2 == 0:
                    for j in range(len(matrix[i])):
                        matrix[i][j] *= 2
        return matrix

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
    imprimirMatriz(matrix, n, m)
    newMatrix = changeMatrix(matrix)
    print("Matriz final:")
    imprimirMatriz(newMatrix, n, m)
    final = "Suma columnas: "
    finallist = []
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += matrix[i][j]
        finallist.append(sum)
    final += ' '.join(map(str, finallist))
    print(final)