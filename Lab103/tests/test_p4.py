from Lib.testInputOutput import set_keyboard_input
from Lib.testInputOutput import get_display_output
import unittest
import random
from gradescope_utils.autograder_utils.decorators import weight, tags
from p4 import main

class TestP4(unittest.TestCase):

    def buildingTests(self, inputList):
        outputList = ["Ingrese numero de filas: ",
                      "Ingrese numero de columnas: ",
                      "Matriz original:",
                      "Matriz final:",
                      "Suma asteriscos: "]
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
            for j in range(4):
                if (i + j) % 2 == 0:
                    self.assertEqual(line[j], '@', f"No estás realizando correctamente el cambio de asteriscos y arrobas.")
                else:
                    self.assertEqual(line[j], '*', f"No estás realizando correctamente el cambio de asteriscos y arrobas.")
    
    @weight(1)
    @tags("Pregunta 4")
    def test_sol(self):
        """Pregunta 4 - Probando solución en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        for i in range(3):
            line = outputAssert[0][7 + i].split()
            for j in range(4):
                if (i + j) % 2 == 0:
                    self.assertEqual(line[j], '@', f"No estás realizando correctamente el cambio de asteriscos y arrobas.")
                else:
                    self.assertEqual(line[j], '*', f"No estás realizando correctamente el cambio de asteriscos y arrobas.")
    
    @weight(0.5)
    @tags("Pregunta 4")
    def test_sum_square(self):
        """Pregunta 4 - Probando suma de asteriscos en matriz cuadrada"""
        outputAssert = self.buildingTests(["4", "4"])
        count = 0
        for i in range(4):
            for j in range(4):
                if (i + j) % 2 != 0:
                    count += 1
        outputAssert[1][4] += str(count)
        self.assertEqual(outputAssert[0][12], outputAssert[1][4], f"No estás sumando correctamente los asteriscos")

    @weight(0.5)
    @tags("Pregunta 4")
    def test_sum(self):
        """Pregunta 4 - Probando suma de asteriscos en matriz no cuadrada"""
        outputAssert = self.buildingTests(["3", "4"])
        count = 0
        for i in range(3):
            for j in range(4):
                if (i + j) % 2 != 0:
                    count += 1
        outputAssert[1][4] += str(count)
        self.assertEqual(outputAssert[0][10], outputAssert[1][4], f"No estás sumando correctamente los asteriscos")

    
if __name__ == '__main__':
    t =  TestP4()
    t.test_input(t)
