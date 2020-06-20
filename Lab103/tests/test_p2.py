from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p2 import main
import random

class TestP2(unittest.TestCase):

    def buildingTests(self,inputList):
        outputList = ["Ingrese nombre del usuario: ",
                      "Ingrese preferencia (especial o numeros): ",
                      "Su nombre sera: "]
        preference = 'numeros' if outputList[1] == '' or (outputList[1] != 'numeros' and outputList[1] != 'especial') else outputList[1]
        newName = '@'.join(inputList[0])
        outputList[2] += newName
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output, outputList]

    @weight(0.5)
    @tags("Pregunta 2")
    def test_empty_preference(self):
        """Pregunta 2 - Probando preferencia vacia"""
        outputAssert = self.buildingTests(["Juan", ""])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        newName = outputAssert[0][2][-7:]
        self.assertEqual(newName[0], 'J', f"No deberías modificar las letras del nombre original.")
        self.assertTrue('0' <= newName[1] <= '9', f"No estás tomando en cuenta la preferencia en números cuando se ingresa vacío.")

    @weight(0.5)
    @tags("Pregunta 2")
    def test_error_preference(self):
        """Pregunta 2 - Probando preferencia erronea"""
        outputAssert = self.buildingTests(["Juan", "mayusculas"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        newName = outputAssert[0][2][-7:]
        self.assertEqual(newName[0], 'J', f"No deberías modificar las letras del nombre original.")
        self.assertTrue('0' <= newName[1] <= '9', f"No estás tomando en cuenta la preferencia en números cuando se ingresa una palabra diferente de números o mayúsculas.")
    
    @weight(2)
    @tags("Pregunta 2")
    def test_especial(self):
        """Pregunta 2 - Probando preferencia especial"""
        outputAssert = self.buildingTests(["Juan", "especial"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(2)
    @tags("Pregunta 2")
    def test_strong(self):
        """Pregunta 2 - Probando preferencia numeros"""
        outputAssert = self.buildingTests(["Juan", "numeros"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        name = "Juan"
        count = 0
        newName = outputAssert[0][2][-7:]
        for i in range(len(newName)):
            if i % 2 == 0:
                self.assertEqual(newName[i], name[count], f"No deberías modificar las letras del nombre original.")
                count += 1
            else:
                self.assertTrue('0' <= newName[i] <= '9', f"El número no está dentro del rango o no estás insertando un número en la posición correcta.")

if __name__ == '__main__':
    t =  TestP2()
    t.test_input(t)
