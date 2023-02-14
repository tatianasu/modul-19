import pytest
from app.calculator import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator
#инициализируем приложение калькулятор.

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

   def test_division_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

   def test_subtraction_correctly(self):
       assert self.calc.subtraction(self, 4, 2) == 2

   def test_adding_correctly(self):
       assert self.calc.adding(self, 4, 2) == 6

   def test_zero_division(self):
       with pytest.raises(ZeroDivisionError):
           self.calc.division(self, 1, 0)


   def teardown(self):
       print('Выполнение метода Teardown')