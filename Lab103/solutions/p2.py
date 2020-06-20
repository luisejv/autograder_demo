def main():
    import random
    def nameGenerator(name, preference):
        newName = ''
        for i in range(len(name)):
            newName += name[i]
            if i != len(name) - 1:
                newName += str(random.randint(0, 9)) if preference == 'numeros' else '@'
        return newName

    name = input('Ingrese nombre del usuario: ')
    preference = input('Ingrese preferencia (especial o numeros): ')
    preference = 'numeros' if preference == '' or (preference != 'numeros' and preference != 'especial') else preference
    print('Su nombre sera: ' + nameGenerator(name, preference))