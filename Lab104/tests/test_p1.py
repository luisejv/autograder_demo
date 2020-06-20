from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p1 import main

class TestP1(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese frase1: ",
                      "Ingrese frase2: ",
                      "Vocales ",
                      "Consonantes ",
                      "Otros caracteres ",
                      "Frase invertida: "]
        vowels1 = 0
        vowels2 = 0
        consonants1 = 0
        consonants2 = 0
        others1 = 0
        others2 = 0
        phrase1 = inputList[0] if len(inputList[0]) == len(inputList[1]) else inputList[2]
        phrase2 = inputList[1] if len(inputList[0]) == len(inputList[1]) else inputList[3]
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
        outputList[2] += "frase1=" + str(vowels1) + ",frase2=" + str(vowels2)
        outputList[3] += "frase1=" + str(consonants1) + ",frase2=" + str(consonants2)
        outputList[4] += "frase1=" + str(others1) + ",frase2=" + str(others2)
        outputList[5] += phrase1[::-1] if others1 > others2 else phrase2[::-1]
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output, outputList]

    @weight(1)
    @tags("Pregunta 1")
    def test_error(self):
        """Pregunta 1 - Probando entradas correctas y erróneas"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo", "Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje debería ser: \"{outputAssert[1][0]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][2], outputAssert[1][0], f"No estás checkeando que los strings tengan la misma longitud")
        self.assertEqual(outputAssert[0][3], outputAssert[1][1], f"No estás checkeando que los strings tengan la misma longitud")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_vowels(self):
        """Pregunta 1 - Probando vocales"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_consonants(self):
        """Pregunta 1 - Probando consonantes"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        self.assertEqual(outputAssert[0][3], outputAssert[1][3], f"El resultado debería ser: \"{outputAssert[1][3]}\"")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_others(self):
        """Pregunta 1 - Probando otros caracteres"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        self.assertEqual(outputAssert[0][4], outputAssert[1][4], f"El resultado debería ser: \"{outputAssert[1][4]}\"")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_inverted(self):
        """Pregunta 1 - Probando frase invertida"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        self.assertEqual(outputAssert[0][5], outputAssert[1][5], f"El resultado debería ser: \"{outputAssert[1][5]}\"")


if __name__ == '__main__':
    t = TestP1()
    t.test_input(t)
