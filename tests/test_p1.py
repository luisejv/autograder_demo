from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags

class TestP1(unittest.TestCase):

    def buildingTests(self,inputList):
        outputList = ["Ingrese frase1: ",
                      "Ingrese frase2: ",
                      "Vocales ",
                      "Consonantes ",
                      "Otros caracteres ",
                      "Frase invertida: "]
        #inputList = ["Exito en la PC2 ICC 103", "Hola mundo programar :)"]
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
        outputList[2] += "frase1=" + vowels1 + ",frase2=" + vowels2
        outputList[3] += "frase1=" + consonants1 + ",frase2=" + consonants2
        outputList[4] += "frase1=" + others1 + ",frase2=" + others2
        outputList[5] = outputList[5] + phrase1[::-1] if others1>others2 else outputList[5] + phrase2[::-1]  
        set_keyboard_input(inputList)
        import p1
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 1")
    def test_input1(self):
        """Frase 1"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][0],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 1")
    def test_input2(self):
        """Frase 2"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][1],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 1")
    def test_output1(self):
        """Salida Vocales"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                        msgUser,
                        f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 1")
    def test_output2(self):
        """Salida Consonantes"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][3]
        self.assertEqual(outputAssert[0][3],
                        msgUser,
                        f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 1")
    def test_output3(self):
        """Salida Otros"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][4]
        self.assertEqual(outputAssert[0][4],
                        msgUser,
                        f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 1")
    def test_output4(self):
        """Salida Frase Invertida"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][5]
        self.assertEqual(outputAssert[0][5],
                        msgUser,
                        f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0.5)
    @tags("Pregunta 1")
    def test_error_1(self):
        """Probando entrada erronea 1"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo", "Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0.5)
    @tags("Pregunta 1")
    def test_error_2(self):
        """Probando entrada erronea 2"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo", "Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][3],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 1")
    def test_vowels(self):
        """Probando resultado vocales"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser = outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 1")
    def test_consonants(self):
        """Probando resultado consonantes"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser =outputAssert[1][3]
        self.assertEqual(outputAssert[0][3],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 1")
    def test_others(self):
        """Probando resultado otros caracteres"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser =outputAssert[1][4]
        self.assertEqual(outputAssert[0][4],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 1")
    def test_inverted(self):
        """Probando resultado invertido"""
        outputAssert = self.buildingTests(["Exito en la PC2 ICC 103", "Hola mundo programar :)"])
        msgUser =outputAssert[1][5]
        self.assertEqual(outputAssert[0][5],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")

if __name__ == '__main__':
    t =  TestP1()
    t.test_input(t)
