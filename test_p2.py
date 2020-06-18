from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags

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
        outputList[2] = name + "buena contrasena" if mayus >= 2 and numbers >= 3 and charsCount >= 1 else name + "contrasena debil"
        set_keyboard_input(inputList)
        import p2
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 2")
    def test_input1(self):
        """Nombre"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][0],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 2")
    def test_input2(self):
        """Contraseña"""
        outputAssert = self.buildingTests(["", ""])
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][1],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 2")
    def test_error(self):
        """Probando contraseña erronea"""
        outputAssert = self.buildingTests(["Juan", "hola MUN1", "ABE123cd$"])
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(1.5)
    @tags("Pregunta 2")
    def test_weak(self):
        """Probando contraseña debil"""
        outputAssert = self.buildingTests(["Juan", "ABB123cd$"])
        msgUser = outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")
    @weight(1.5)
    @tags("Pregunta 2")
    def test_strong(self):
        """Probando contraseña fuerte"""
        outputAssert = self.buildingTests(["Juan", "ABE123cd$"])
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 2")
    def test_name(self):
        """Probando sin nombre"""
        outputAssert = self.buildingTests(["", "ABE123cd$"])
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El resultado debería ser: \"{msgUser}\"")

if __name__ == '__main__':
    t =  TestP2()
    t.test_input(t)
