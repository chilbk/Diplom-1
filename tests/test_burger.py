from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import textwrap


class TestBurger:
# Метод test_set_buns проверяет, что метод set_buns корректно сохраняет выбранную булочку
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Булочка ржаная', 100)
        burger.set_buns(bun)

        assert burger.bun is bun

# Метод test_add_ingredient проверяет, что метод add_ingredient добавляет ингредиент в список
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 50)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

# Метод test_remove_ingredient проверяет, что метод remove_ingredient удаляет ингредиент из списка
    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 150)
        ing2 = Ingredient(INGREDIENT_TYPE_SAUCE, 'mustard', 30)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

# Метод test_move_ingredient проверяет, что метод move_ingredient перемещает ингредиент в другую позицию списка
    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'bbq', 40)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, 'lettuce', 20)
        ing3 = Ingredient(INGREDIENT_TYPE_FILLING, 'cheese', 60)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(2, 0)
        assert burger.ingredients == [ing3, ing1, ing2]

# Метод test_get_price проверяет, что метод get_price возвращает правильную цену
    def test_get_price(self):
        burger = Burger()
        burger.set_buns(Bun('black bun', 100))  # *2 = 200
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 50))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 150))

        total = burger.get_price()
        assert total == 200 + 50 + 150

# Метод test_get_receipt проверяет, что метод get_receipt возвращает правильный чек, включая верную сумму и названия
    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(Bun('red bun', 120))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'cheese', 70))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'mayo', 30))

        receipt = burger.get_receipt()

        expected_receipt = textwrap.dedent("""\
            (==== red bun ====)
            = filling cheese =
            = sauce mayo =
            (==== red bun ====)

            Price: 340""")   # 2 булочки по 120 + сыр за 70 + майонез за 30

        assert receipt == expected_receipt