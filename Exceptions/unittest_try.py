import unittest
from collections import defaultdict
import os
import sys


def cube(n):
    return n ** 3


def triarea(base, height):
    return base * height / 2


def holi():
    return "holi"


class MyTest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(5), 125)
        self.assertEqual(cube(10), 1000)
        self.assertEqual(cube(0), 0)

    def test_triarea(self):
        self.assertEqual(triarea(10, 10), 50)

    def test_holi(self):
        self.assertEqual(holi(), "holi")


class MostrarAsserts(unittest.TestCase):

    def test_aserciones(self):
        a = 2
        b = a
        c = 1. + 1.
        self.assertEqual([1, 2, 3], [1, 2, 3])
        self.assertNotEqual("hola", "chao")
        self.assertTrue("Hola", "Hola")
        self.assertFalse("Hola" == "Chao")
        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNotNone(2)
        self.assertIn(2, [2, 3, 4])
        self.assertNotIn(1, [2, 3, 4])
        self.assertIsInstance("Hola", str)
        self.assertNotIsInstance("1", int)


def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_python30_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    def test_python31_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])


class ListaEstadisticas(list):
    def media(self):
        return sum(self) / len(self)

    def mediana(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx - 1]) / 2

    def moda(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        moda_freq = max(freqs.values())
        modas = []
        for item, value in freqs.items():
            if value == moda_freq:
                modas.append(item)
        return modas


class TestearEstadisticas(unittest.TestCase):

    def setUp(self):
        self.stats = ListaEstadisticas([1, 2, 2, 3, 3, 4])

    def test_media(self):
        print(self.stats)
        self.assertEqual(self.stats.media(), 2.5)

    def test_mediana(self):
        self.assertEqual(self.stats.mediana(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.mediana(), 3)

    def test_moda(self):
        print(self.stats)
        self.assertEqual(self.stats.moda(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.moda(), [3])


class TestearArchivo(unittest.TestCase):

    def setUp(self):
        self.archivo = open("prueba.txt", 'w')
        self.diccionario = {1: "Hola", 2: "Chao"}

    def tearDown(self):
        self.archivo.close()
        print("Eliminando archivos temporales...")
        os.remove("prueba.txt")

    def test_str(self):
        print("escribiendo archivo temporal...")
        self.archivo.write(self.diccionario[1])
        self.archivo.close()
        self.archivo = open("prueba.txt", 'r')
        d = self.archivo.readlines()[0]
        print(d)
        self.assertEqual(self.diccionario[1], d)


class IgnorarTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_falla(self):
        self.assertEqual(False, True)

    @unittest.skip("Test inútil")
    def test_ignorar(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 1, "no funciona en 3.1")
    def test_ignorar_if(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'), "no funciona en linux")
    def test_ignorar_unless(self):
        self.assertEqual(False, True)


suite = unittest.TestLoader().loadTestsFromTestCase(IgnorarTests)
unittest.TextTestRunner().run(suite)
