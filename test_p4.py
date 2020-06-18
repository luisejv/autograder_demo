from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags

class TestP4(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese numero de filas: ",
                      "Ingrese numero de columnas: ",
                      "Matriz original:",
                      "Matriz final:"]
        #inputList = ["3", "3"]
        set_keyboard_input(inputList)
        import p4
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 4")
    def test_input1(self):
        """Probando entrada 1"""
        outputAssert = self.buildingTests(["2", "2"])
        msgUser =outputAssert[1][0]
        self.assertEqual(outputAssert[0][0],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 4")
    def test_input2(self):
        """Probando entrada 2"""
        outputAssert = self.buildingTests(["2", "2"])
        msgUser =outputAssert[1][1]
        self.assertEqual(outputAssert[0][1],
                         msgUser,
                         f"El mensaje de entrada hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 4")
    def test_output1(self):
        """Probando salida 1"""
        outputAssert = self.buildingTests(["2", "2"])
        msgUser =outputAssert[1][2]
        self.assertEqual(outputAssert[0][2],
                         msgUser,
                         f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(0)
    @tags("Pregunta 4")
    def test_output2(self):
        """Probando salida 2"""
        outputAssert = self.buildingTests(["2", "2"])
        msgUser =outputAssert[1][3]
        self.assertEqual(outputAssert[0][5],
                         msgUser,
                         f"El mensaje de salida hacia el usuario debería ser: \"{msgUser}\"")
    @weight(1)
    @tags("Pregunta 4")
    def test_values_square(self):
        """Probando rango valores en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        for i in range(4):
            line = outputAssert[0][3 + i].split()
            self.assertTrue(len(line), 4)
            for j in range(4):
                self.assertTrue(0 <= line[j] <= 10)
    @weight(1)
    @tags("Pregunta 4")
    def test_values(self):
        """Probando rango valores en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        for i in range(3):
            line = outputAssert[0][3 + i].split()
            self.assertTrue(len(line), 4)
            for j in range(4):
                self.assertTrue(0 <= line[j] <= 10)
    @weight(1.5)
    @tags("Pregunta 4")
    def test_sol_square(self):
        """Probando solución en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        for i in range(4):
            line = outputAssert[0][8 + i].split()
            line2 = outputAssert[0][3 + i].split()
            for j in range(4):
                if i % 2 != 0:
                    self.assertTrue(int(line[j]), int(line2[j]) + 1)
                else:
                    self.assertTrue(line[j], line2[j])
    @weight(1.5)
    @tags("Pregunta 4")
    def test_sol(self):
        """Probando solución en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        for i in range(3):
            line = outputAssert[0][7 + i].split()
            line2 = outputAssert[0][3 + i].split()
            for j in range(4):
                if i % 2 != 0:
                    self.assertTrue(line[j], line2[j])
                else:
                    self.assertTrue(int(line[j]), int(line2[j])*2)
    
if __name__ == '__main__':
    t =  TestP4()
    t.test_input(t)
