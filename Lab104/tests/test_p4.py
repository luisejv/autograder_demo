from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from p4 import main

class TestP4(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese numero de filas: ",
                      "Ingrese numero de columnas: ",
                      "Matriz original:",
                      "Matriz final:",
                      "Suma columnas: "]
        #inputList = ["3", "3"]
        set_keyboard_input(inputList)
        main()
        output = get_display_output()
        return [output,outputList]

    @weight(0)
    @tags("Pregunta 4")
    def test_input(self):
        """Pregunta 4 - Probando entradas y salidas"""
        outputAssert = self.buildingTests(["2", "2"])
        self.assertEqual(outputAssert[0][0], outputAssert[1][0], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][0]}\"")
        self.assertEqual(outputAssert[0][1], outputAssert[1][1], f"El mensaje de entrada hacia el usuario debería ser: \"{outputAssert[1][1]}\"")
        self.assertEqual(outputAssert[0][2], outputAssert[1][2], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][2]}\"")
        self.assertEqual(outputAssert[0][5], outputAssert[1][3], f"El mensaje de salida hacia el usuario debería ser: \"{outputAssert[1][3]}\"")
    
    @weight(1)
    @tags("Pregunta 4")
    def test_values_square(self):
        """Pregunta 4 - Probando rango valores en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        for i in range(4):
            line = outputAssert[0][3 + i].split()
            self.assertEqual(len(line), 4, f"La matriz no tiene 4 columnas.")
            for j in range(4):
                self.assertTrue(0 <= int(line[j]) <= 10, f"Número no está dentro del rango.")
    @weight(1)
    @tags("Pregunta 4")
    def test_values(self):
        """Pregunta 4 - Probando rango valores en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        for i in range(3):
            line = outputAssert[0][3 + i].split()
            self.assertEqual(len(line), 4, f"La matriz no tiene 4 columnas.")
            for j in range(4):
                self.assertTrue(0 <= int(line[j]) <= 10, f"Número no está dentro del rango.")
    @weight(1)
    @tags("Pregunta 4")
    def test_sol_square(self):
        """Pregunta 4 - Probando solución en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        for i in range(4):
            line = outputAssert[0][8 + i].split()
            line2 = outputAssert[0][3 + i].split()
            for j in range(4):
                if i % 2 != 0:
                    self.assertEqual(int(line[j]), int(line2[j]) + 1, f"No has realizado correctamente el cambio a la matriz")
                else:
                    self.assertEqual(line[j], line2[j], f"No debes cambiar los valores en esta posición. No has realizado correctamente el cambio a la matriz")
    @weight(1)
    @tags("Pregunta 4")
    def test_sol(self):
        """Pregunta 4 - Probando solución en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        for i in range(3):
            line = outputAssert[0][7 + i].split()
            line2 = outputAssert[0][3 + i].split()
            for j in range(4):
                if i % 2 != 0:
                    self.assertEqual(line[j], line2[j], f"No debes cambiar los valores en esta posición. No has realizado correctamente el cambio a la matriz")
                else:
                    self.assertEqual(int(line[j]), int(line2[j]) * 2, f"No has realizado correctamente el cambio a la matriz")
                    
    @weight(0.5)
    @tags("Pregunta 4")
    def test_sum_square(self):
        """Pregunta 4 - Probando suma de columnas en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        finallist = []
        for j in range(4):
            sum = 0
            for i in range(4):
                line = outputAssert[0][8 + i].split()
                sum += int(line[j])
            finallist.append(sum)
        outputAssert[1][4] += ' '.join(map(str, finallist))
        self.assertEqual(outputAssert[0][12], outputAssert[1][4], f"No estás sumando correctamente las columnas")

    @weight(0.5)
    @tags("Pregunta 4")
    def test_sum(self):
        """Pregunta 4 - Probando suma de columnas en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        finallist = []
        for j in range(4):
            sum = 0
            for i in range(3):
                line = outputAssert[0][7 + i].split()
                sum += int(line[j])
            finallist.append(sum)
        outputAssert[1][4] += ' '.join(map(str, finallist))
        self.assertEqual(outputAssert[0][10], outputAssert[1][4], f"No estás sumando correctamente las columnas")
    
if __name__ == '__main__':
    t =  TestP4()
    t.test_input(t)
