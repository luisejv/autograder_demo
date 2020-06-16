import random

def question1():
    finish = False
    while not finish:
        phrase1 = input("Ingrese frase1: ")
        phrase2 = input("Ingrese frase2: ")
        finish = len(phrase1) == len(phrase2)

    vowels1 = 0
    vowels2 = 0
    consonants1 = 0
    consonants2 = 0
    others1 = 0
    others2 = 0
    for i in range(len(phrase1)):
        if phrase1[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels1 += 1
        elif phrase1[i].lower() < 'a' or phrase1[i].lower() > 'z':
            others1 += 1
        else:
            consonants1 += 1

        if phrase2[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels2 += 1
        elif phrase2[i].lower() < 'a' or phrase2[i].lower() > 'z':
            others2 += 1
        else:
            consonants2 += 1

    print("Vocales frase1 =", vowels1, ", frase2 =", vowels2)
    print("Consonantes frase1 =", consonants1, ", frase2 =", consonants2)
    print("Otros caracteres frase1 =", others1, ", frase2 =", others2)

    inverted = ""
    if others2 > others1:
        inverted = phrase2[::-1]
    else:
        inverted = phrase1[::-1]

    print("Frase invertida: " + inverted)

def validacion(password):
    whiteSpaces = 0
    for i in range(len(password)):
        if password[i] == " ":
            whiteSpaces += 1
    return whiteSpaces == 0 and len(password) == 9

def validate(password, name):
    name = "Test" if name == "" else name
    mayus = 0
    numbers = 0
    chars = ["$", "#", "&", "*", "!", "?"]
    charsCount = 0
    for i in range(len(password)):
        if password[i] in chars:
            charsCount += 1
        elif password[i] in ['A', 'E', 'I', 'O', 'U']:
            mayus += 1
        elif password[i] >= '0' and password[i] <= '9':
            numbers += 1
    if mayus >= 2 and numbers >= 3 and charsCount >= 1:
        print(name, "buena contrasena")
    else:
        print(name, "contrasena debil")

def question2():
    name = input("Ingrese nombre del usuario: ")
    password = ""
    finished = False
    while not finished:
        password = input("Ingrese contrasena (tamanio 9): ")
        finished = validacion(password)
    validate(password, name)
        
def desordenar(lista):
    random.seed(None)
    for i in range(len(lista)):
        num = random.randint(0, len(lista)-1)
        aux = lista[i]
        lista[i] = lista[num]
        lista[num] = aux

def question3():
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

def imprimirMatriz(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

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

def question4():
    finished = False
    while not finished:
        n = int(input("Ingrese numero de filas: "))
        m = int(input("Ingrese numero de columnas: "))
        finished = n > 0 and m > 0
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(0, 10))
        matrix.append(row)
    print("Matriz original: ")
    imprimirMatriz(matrix, n, m)
    newMatrix = changeMatrix(matrix)
    print("Matriz final: ")
    imprimirMatriz(newMatrix, n, m)
    print("Suma columnas:", end=" ")
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += matrix[i][j]
        print(sum, end=" ")
    print()
            

finished = False
while not finished:
    question = int(input("Pregunta n: "))

    if question == 1:
        question1()
    elif question == 2:
        question2()
    elif question == 3:
        question3()
    elif question == 4:
        question4()
    
    finished = question == 0





    
    
    





