def main():
    phrase = input("Ingrese frase:")
    print("Frase:" + phrase)
    minus = 0
    mayus = 0
    caracs = 0
    nums = 0
    sumnums = 0
    strnums = ""
    for i in phrase:
        if i >= 'a' and i <= 'z':
            minus += 1
        elif i >= 'A' and i <= 'Z':
            mayus += 1
        elif i >= '0' and i <= '9':
            nums += 1
            sumnums += int(i)
            strnums += i
        else:
            caracs += 1
    print('Mayusculas:' + str(mayus))
    print('Minusculas:' + str(minus))
    #Imprimir la cantidad de numeros no estaba considerado en el
    #ejemplo pero si en el enunciado de la pregunta
    #Igual se tomara en cuenta como si no se hubiera pedido
    print('Numeros:' + str(nums))
    print('Caracteres especiales:' + str(caracs))
    print('Suma numeros:' + str(sumnums))
    print('String numeros:' + strnums)
