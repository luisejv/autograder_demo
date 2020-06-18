from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags

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
        outputList[2] += listaStr
        set_keyboard_input(inputList)
        import p3
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 3")
    def test_input1(self):
        """Probando mensaje 1"""
        lista = []
        for i in range(10):
            lista.append("")
        outputAssert = self.buildingTests(lista)
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][0],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 3")
    def test_input5(self):
        """Probando mensaje 5"""
        lista = []
        for i in range(10):
            lista.append("")
        outputAssert = self.buildingTests(lista)
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][4],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 3")
    def test_input10(self):
        """Probando mensaje 10"""
        lista = []
        for i in range(10):
            lista.append("")
        outputAssert = self.buildingTests(lista)
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][9],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 3")
    def test_output1(self):
        """Probando salida 1"""
        lista = []
        for i in range(10):
            lista.append("")
        outputAssert = self.buildingTests(lista)
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][10],
                         msgUser,
                         f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 3")
    def test_output2(self):
        """Probando salida 2"""
        lista = []
        for i in range(10):
            lista.append("")
        outputAssert = self.buildingTests(lista)
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][11],
                        msgUser,
                        f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(2.5)
    @tags("Pregunta 3")
    def test_list(self):
        """Salida Lista"""
        outputAssert = self.buildingTests(["3", "3", "20", "100", "1", "14.2", "5", "999", "20.2", "14.2"])
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][10],
                        msgUser,
                        f"El resultado debería ser: \"{msgUser}\"")
    @weight(2.5)
    @tags("Pregunta 3")
    def test_list2(self):
        """Salida Lista Desordenada"""
        lista = ["3", "3", "20", "100", "1", "14.2", "5", "999", "20.2", "14.2"]
        outputAssert = self.buildingTests(lista)
        listaStr = "" + str(lista[0])
        for i in range(1, len(lista)):
            listaStr += "," + str(lista[i])
        self.assertNotEqual(outputAssert[0][11],
                        listaStr,
                        "La lista no está desordenada")
    
if __name__ == '__main__':
    t =  TestP3()
    t.test_input(t)
