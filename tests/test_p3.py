from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p3 import main

class TestP3(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese valor para la lista: ",
                      "Lista: ",
                      "Lista desordenada: "]
        #inputList = ["3", "3", "20", "100", "1", "14.2", "5", "999", "20.2", "14.2"]
        lista = []
        for i in range(10):
            lista.append(inputList[i])
        listaStr = "" + str(lista[0])
        for i in range(1, len(lista)):
            listaStr += "," + str(lista[i])
        outputList[1] += listaStr
        outputList[2] += listaStr
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
        self.assertEqual(outputAssert[0][9], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][0]}\"")

    @weight(0)
    @tags("Pregunta 3")
    def test_output(self):
        """Pregunta 3 - Probando salidas"""
        lista = []
        for i in range(10):
            lista.append("0")
        outputAssert = self.buildingTests(lista)
        self.assertEqual(outputAssert[0][10], outputAssert[1][1], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][11], outputAssert[1][2], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(2.5)
    @tags("Pregunta 3")
    def test_list(self):
        """Pregunta 3 - Salida Lista"""
        outputAssert = self.buildingTests(["3", "3", "20", "100", "1", "14", "5", "999", "20", "15"])
        self.assertEqual(outputAssert[0][10], outputAssert[1][1], f"El resultado debería ser: \"{outputAssert[1][2]}\"")

    @weight(2.5)
    @tags("Pregunta 3")
    def test_unordered_list(self):
        """Pregunta 3 - Salida Lista Desordenada"""
        outputAssert = self.buildingTests(["3", "3", "20", "100", "1", "14", "5", "999", "20", "15"])
        self.assertNotEqual(outputAssert[0][11], outputAssert[1][2], f"No estás desordenando la lista de manera aleatoria")
    
if __name__ == '__main__':
    t =  TestP3()
    t.test_input(t)
