from main import Ingredient, Receipt
import unittest

class TestReceipt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед всеми тестами."""
        cls.receipt_name = 'Гирос'
        cls.receipt_ingredients_data = [
            ("Куриное филе", 500, 400, 300),
            ("Пита", 200, 200, 100),
            ("Томат", 150, 140, 60),
            ("Красный лук", 100, 95, 30),
            ("Цацики", 150, 150, 50),
            ("Картофель фри", 300, 300, 120),
            ("Оливковое масло", 20, 20, 10),
        ]

    def setUp(self):
        """Вызывается перед каждым тестом."""
        self.receipt = Receipt(self.receipt_name, self.receipt_ingredients_data)

    def test_receipt_name(self):
        self.assertEqual(self.receipt._title, 'Гирос')

    def test_calc_cost(self):
        self.assertEqual(self.receipt.calc_cost(), 670)

    def test_calc_cost_with_portions(self):
        self.assertEqual(self.receipt.calc_cost(portions=2), 1340)





    @classmethod
    def tearDownClass(cls):
        """Вызывается один раз после всех тестов."""
        print("tearDownClass: Завершение тестов класса.")



if __name__ == "__main__":
    unittest.main()
