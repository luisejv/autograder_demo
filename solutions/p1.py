def main():
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

    print("Vocales frase1=" + str(vowels1) + ",frase2=" + str(vowels2))
    print("Consonantes frase1=" + str(consonants1) + ",frase2=" + str(consonants2))
    print("Otros caracteres frase1=" + str(others1) + ",frase2=" + str(others2))

    inverted = ""
    if others2 > others1:
        inverted = phrase2[::-1]
    else:
        inverted = phrase1[::-1]

    print("Frase invertida: " + inverted)
