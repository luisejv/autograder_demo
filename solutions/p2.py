def main():
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
            print(name + " buena contrasena")
        else:
            print(name + " contrasena debil")

    name = input("Ingrese nombre del usuario: ")
    password = ""
    finished = False
    while not finished:
        password = input("Ingrese contrasena (tamano 9): ")
        finished = validacion(password)
    validate(password, name)