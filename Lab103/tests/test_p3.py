from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p3 import main

class TestP3(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese valor para lista numeros: ",
                      "Ingrese valor para lista palabras: ",
                      "Numeros: ",
                      "Palabras: ",
                      "Tamano numeros: ",
                      "Tamano palabras: ",
                      "Lista tamano: "]
        numbers = inputList[:5]
        words = inputList[5:]
        outputList[2] += ','.join(numbers)
        outputList[3] += ','.join(words)
        numlen = [len(i) for i in numbers]
        strlen = [len(i) for i in words]
        outputList[4] += ','.join(map(str,numlen))
        outputList[5] += ','.join(map(str,strlen))
        numlen = [i for i in numlen if i != max(numlen)]
        strlen = [i for i in strlen if i != max(strlen)]
        final = numlen + strlen
        outputList[6] += ','.join(map(str,final))
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 3")
    def test_input(self):
        """Pregunta 3 - Probando mensaje de entradas 1, 5, 10"""
        lista = []
        for i in range(10):
            lista.append("0")
        outputAssert = self.buildingTests(lista)
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][0]}\"")
        self.assertEqual(outputAssert[0][4], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][0]}\"")
        self.assertEqual(outputAssert[0][9], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")

    @weight(0)
    @tags("Pregunta 3")
    def test_output(self):
        """Pregunta 3 - Probando salidas"""
        lista = []
        for i in range(10):
            lista.append("0")
        outputAssert = self.buildingTests(lista)
        self.assertEqual(outputAssert[0][10], outputAssert[1][2], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][2]}\"")
        self.assertEqual(outputAssert[0][11], outputAssert[1][3], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][3]}\"")
        self.assertEqual(outputAssert[0][12], outputAssert[1][4], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][4]}\"")
        self.assertEqual(outputAssert[0][13], outputAssert[1][5], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][5]}\"")
        self.assertEqual(outputAssert[0][14], outputAssert[1][6], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][6]}\"")
    
    @weight(1)
    @tags("Pregunta 3")
    def test_numbers(self):
        """Pregunta 3 - Salida Números"""
        outputAssert = self.buildingTests(["3", "3", "20", "450", "11", "hola", "programar", "icc", "programar", "test"])
        self.assertEqual(outputAssert[0][10], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")

    @weight(1)
    @tags("Pregunta 3")
    def test_words(self):
        """Pregunta 3 - Salida Palabras"""
        outputAssert = self.buildingTests(["3", "3", "20", "450", "11", "hola", "programar", "icc", "programar", "test"])
        self.assertEqual(outputAssert[0][11], outputAssert[1][3], f"El resultado debería ser: \"{outputAssert[1][3]}\"")
    
    @weight(1)
    @tags("Pregunta 3")
    def test_len_numbers(self):
        """Pregunta 3 - Salida tamaño números"""
        outputAssert = self.buildingTests(["3", "3", "20", "450", "11", "hola", "programar", "icc", "programar", "test"])
        self.assertEqual(outputAssert[0][12], outputAssert[1][4], f"El resultado debería ser: \"{outputAssert[1][4]}\"")
    
    @weight(1)
    @tags("Pregunta 3")
    def test_len_words(self):
        """Pregunta 3 - Salida tamaño palabras"""
        outputAssert = self.buildingTests(["3", "3", "20", "450", "11", "hola", "programar", "icc", "programar", "test"])
        self.assertEqual(outputAssert[0][13], outputAssert[1][5], f"El resultado debería ser: \"{outputAssert[1][5]}\"")
    
    @weight(1)
    @tags("Pregunta 3")
    def test_final(self):
        """Pregunta 3 - Salida final"""
        outputAssert = self.buildingTests(["3", "3", "20", "450", "11", "hola", "programar", "icc", "programar", "test"])
        self.assertEqual(outputAssert[0][14], outputAssert[1][6], f"El resultado debería ser: \"{outputAssert[1][6]}\"")
    
if __name__ == '__main__':
    t =  TestP3()
    t.test_input(t)
