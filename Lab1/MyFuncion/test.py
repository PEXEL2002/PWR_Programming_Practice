import unittest
from main import Add

class Test(unittest.TestCase):
    def testAdd1(self):
        a=Add("")
        self.assertEqual(a, 0)
    def testAdd2(self):
        a=Add("2,2")
        self.assertEqual(a, 4)
    def testAdd3(self):
        a=Add("0,0")
        self.assertEqual(a, 0)
    def testAdd4(self):
        a = Add("1.2")
        self.assertEqual(a, 1.2)

    def testAddMulti1(self):
        a=Add("1,1,1")
        self.assertEqual(a,3)

    def testAddNew1(self):
        a=Add("1\n2\n2")
        self.assertEqual(a,5)

    def testAddNew2(self):
        with self.assertRaises(ValueError):
            a=Add("1,\n2")




