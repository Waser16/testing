class Ingredient:
    """Ингредиент"""

    def __init__(
        self,
        name: str,
        raw_weight: float,
        weight: float,
        cost: float
    ) -> None:
        self.name = name
        self.raw_weight = raw_weight
        self.weight = weight
        self.cost = cost

    # Валидация для name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Название ингредиента должно быть строкой и не пустым")
        self._name = value

    # Валидация для raw_weight
    @property
    def raw_weight(self):
        return self._raw_weight

    @raw_weight.setter
    def raw_weight(self, value):
        if value <= 0:
            raise ValueError("Вес сырого продукта должен быть положительным числом")
        self._raw_weight = value

    # Валидация для cooked_weight
    @property
    def cooked_weight(self):
        return self._cooked_weight

    @cooked_weight.setter
    def cooked_weight(self, value):
        if value <= 0:
            raise ValueError("Вес готового продукта должен быть положительным числом")
        self._cooked_weight = value

    # Валидация для cost
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError("Стоимость должна быть положительным числом.")
        self._cost = value

    def __str__(self) -> str:
        return f'{self.name}\n сырой вес: {self.raw_weight}\n готовый вес: {self.weight}\n цена: {self.cost}'


class Receipt:
    """Receipt"""

    def __init__(self,
        title: str,
        ingredient_list: list[tuple[str, int, int, int]]
    ):
        self.title = title
        self.ingredient_list = [Ingredient(*ingredient) for ingredient in ingredient_list]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError('Название должно быть строковым значением')
        self._title = value;

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[tuple[str, int, int, int]]) -> None:
        if not ingredients:
            raise ValueError('Список ингредиентов не должен быть пустым')
        if not all(isinstance(item, Ingredient) for item in ingredients):
            raise ValueError('Каждый элемент списка должны быть объектом класса Ingredient')
        self._ingredients = ingredients


    def calc_cost(self, portions: int = 1) -> int:
        return sum(ingredient.cost for ingredient in self.ingredient_list) * portions

    def calc_weight(self, portions: int = 1) -> int:
        return sum(ingredient.weight for ingredient in self.ingredient_list)

    def __str__(self) -> str:
        ingredients_str = '\n'.join(str(ingredient) for ingredient in self.ingredient_list)
        return f'{self.title}\n {ingredients_str}'


if __name__ == '__main__':

    # (Г)алиуллин -> (Г)ирос
    receipt_from_api = {
        "title": "Гирос",
        "ingredients_list": [
            ("Куриное филе", 500, 400, 300),
            ("Пита", 200, 200, 100),
            ("Томат", 150, 140, 60),
            ("Красный лук", 100, 95, 30),
            ("Цацики", 150, 150, 50),
            ("Картофель фри", 300, 300, 120),
            ("Оливковое масло", 20, 20, 10),
        ],
    }
    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])
    print(receipt.__str__(), f'\nОбщая цена: {receipt.calc_cost()}')
    print('---------------------------------------')

    # (А)ртур -> (А)нглийский маффин
    receipt_from_api = {
        "title": "Английский маффин",
        "ingredients_list": [
            ("Мука", 300, 300, 50),
            ("Молоко", 200, 200, 20),
            ("Сухие дрожжи", 7, 7, 15),
            ("Сахар", 20, 20, 5),
            ("Соль", 5, 5, 1),
            ("Сливочное масло", 50, 50, 30),
            ("Кукурузная мука", 30, 30, 10),
        ],
    }
    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])
    print(receipt.__str__(), f'\nОбщая цена: {receipt.calc_cost()}')





