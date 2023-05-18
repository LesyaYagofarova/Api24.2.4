import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 3, 4) == 7

    def test_multiply(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_division(self):
        assert self.calc.division(self, 21, 7) == 3

    def test_subtraction(self):
        assert self.calc.subtraction(self, 21, 7) == 14

    def teardown(self):
        print('Выполнение метода Teardown')




