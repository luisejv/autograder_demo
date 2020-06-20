from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p1 import main

class TestP1(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese frase:",
                      "Frase:",
                      "Mayusculas:",
                      "Minusculas:",
                      "Numeros:",
                      "Caracteres especiales:",
                      "Suma numeros:",
                      "String numeros:"]
        phrase = inputList[0]
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
        outputList[1] += phrase
        outputList[2] += str(mayus)
        outputList[3] += str(minus)
        outputList[4] += str(nums)
        outputList[5] += str(caracs)
        outputList[6] += str(sumnums)
        outputList[7] += strnums
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output, outputList]

    @weight(0.75)
    @tags("Pregunta 1")
    def test_output(self):
        """Pregunta 1 - Probando impresión frase"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje debería ser: \"{outputAssert[1][0]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"La salida debería ser: \"{outputAssert[1][1]}\"")
    
    @weight(0.75)
    @tags("Pregunta 1")
    def test_mayus(self):
        """Pregunta 1 - Probando mayúsculas"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(0.75)
    @tags("Pregunta 1")
    def test_minus(self):
        """Pregunta 1 - Probando minúsculas"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertEqual(outputAssert[0][3], outputAssert[1][3], f"El resultado debería ser: \"{outputAssert[1][3]}\"")
    
    @weight(0.75)
    @tags("Pregunta 1")
    def test_others(self):
        """Pregunta 1 - Probando caracteres especiales"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertTrue((outputAssert[0][4] == outputAssert[1][4] and outputAssert[0][5] == outputAssert[1][5]) ^ (outputAssert[0][4] == outputAssert[1][5]) , f"El resultado debería ser: \"{outputAssert[1][5]}\"")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_sum(self):
        """Pregunta 1 - Probando suma números"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertEqual(outputAssert[0][-2], outputAssert[1][-2], f"El resultado debería ser: \"{outputAssert[1][-2]}\"")
    
    @weight(1)
    @tags("Pregunta 1")
    def test_string(self):
        """Pregunta 1 - Probando string números"""
        outputAssert = self.buildingTests(["Hola me gust@ programar en ICC 1.03"])
        self.assertEqual(outputAssert[0][-1], outputAssert[1][-1], f"El resultado debería ser: \"{outputAssert[1][-1]}\"")


if __name__ == '__main__':
    t = TestP1()
    t.test_input(t)
