import unittest
from division import dividir

class TestStumar(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(3,2),1)
        self.assertEqual(dividir(1,1),1)
        self.assertEqual(dividir(5,1),5)



if __name__== "__main__":
    unittest.main()