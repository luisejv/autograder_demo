from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p2 import main


class TestP2(unittest.TestCase):

    def buildingTests(self,inputList):
        outputList = ["Ingrese nombre del usuario: ",
                      "Ingrese contrasena (tamano 9): ",
                      ""]
        #inputList = ["Juan", "ABE123cd$"]
        name = "Test" if inputList[0] == "" else inputList[0]
        password = ""
        finished = False
        cont = 0
        while not finished:
            cont += 1
            password = inputList[cont]
            whiteSpaces = 0
            for i in range(len(password)):
                if password[i] == " ":
                    whiteSpaces += 1
            finished = whiteSpaces == 0 and len(password) == 9
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
        outputList[2] = name + " buena contrasena" if mayus >= 2 and numbers >= 3 and charsCount >= 1 else name + " contrasena debil"
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output, outputList]

    @weight(1)
    @tags("Pregunta 2")
    def test_error(self):
        """Pregunta 2 - Probando contraseña erronea"""
        outputAssert = self.buildingTests(["Juan", "", "hola MUN1", "ABE123cd$"])
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][2], outputAssert[1][1], f"No estás validando que la contraseña tenga 9 caracteres")
        self.assertEqual(outputAssert[0][3], outputAssert[1][1], f"No estás validando que la contraseña no tenga espacios")
    
    @weight(1.5)
    @tags("Pregunta 2")
    def test_weak(self):
        """Pregunta 2 - Probando contraseña debil"""
        outputAssert = self.buildingTests(["Juan", "ABB123cd$"])
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(1.5)
    @tags("Pregunta 2")
    def test_strong(self):
        """Pregunta 2 - Probando contraseña fuerte"""
        outputAssert = self.buildingTests(["Juan", "ABE123cd$"])
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")
    
    @weight(1)
    @tags("Pregunta 2")
    def test_name(self):
        """Pregunta 2 - Probando sin nombre"""
        outputAssert = self.buildingTests(["", "ABE123cd$"])
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El resultado debería ser: \"{outputAssert[1][2]}\"")

if __name__ == '__main__':
    t =  TestP2()
    t.test_input(t)
