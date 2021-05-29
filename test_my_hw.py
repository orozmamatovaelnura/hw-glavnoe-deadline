import unittest 
from ele import Circle
from ele import Triangle
from ele import Rectangle

class TestHW(unittest.TestCase):
    def setUp(self):
        c=Circle(4,'blue')
        r=Rectangle(3,6,'white')
        t=Triangle(5,5)
    
    def test_show_color(self):
        self.assertEqual(c.show_color(),'blue')
        self.assertEqual(r.show_color(),'white')
        self.assertEqual(t.show_color(),'black')
    def test_circle(self):
        self.assertEqual(c.__sub__(r),32.24)
        self.assertEqual(c.__sub__(t),37.74)
        self.assertEqual(c.__add__(r),68.24000000000001)
        self.assertEqual(c.__add__(t),62.74)
        self.assertEqual(c.__cmp__(r),'Circle > Rectangle')
        self.assertEqual(c.__cmp__(t),'Circle > Triangle')
    def test_rectangle(self):
        self.assertEqual(r.__sub__(c),'ArithmeticError has ocured !')
        self.assertEqual(r.__sub__(t),5.5)
        self.assertEqual(r.__add__(c),68.24000000000001)
        self.assertEqual(r.__add__(t),30.05)
        self.assertEqual(r.__cmp__(c),'Rectangle < Circle')
        self.assertEqual(r.__cmp__(t),'Rectangle > Triangle')
    def test_triangle(self):
        self.assertEqual(t.__sub__(r),'ArithmeticError has ocured !')
        self.assertEqual(t.__sub__(c),'ArithmeticError has ocured !')
        self.assertEqual(t.__add__(r),30.05)
        self.assertEqual(t.__add__(c),62.74)
        self.assertEqual(t.__cmp__(r),'Triangle < Rectangle')
        self.assertEqual(t.__cmp__(c),'Triangle < Circle')
    def test_new_color(self):
        new_r=Rectangle(4,4,'red')
        self.assertEqual(new_r.show_color(),'red')
