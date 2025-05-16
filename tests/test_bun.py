import pytest
from praktikum.bun import Bun

class TestBun():
    @pytest.mark.parametrize("name, price", [("White", 1550.0), ("Red", 1175.5), ("Black", 1080.0)])
    def test_get_name_and_price(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_two_instances_are_independent(self):
        bun1 = Bun("SuperBun", 1000.0)
        bun2 = Bun("ExtraBun", 2070.0)
        assert bun1 is not bun2
        assert bun1.get_name() != bun2.get_name()
        assert bun1.get_price() != bun2.get_price()