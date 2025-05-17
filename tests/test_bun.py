import generators
from data import DataBun
from praktikum.bun import Bun

class TestBun:
    def test_bun_name(self):
        bun_name = generators.generate_word()
        bun_price = generators.generate_price()
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name
        assert bun.price == bun_price

    def test_get_bun_name(self, create_bun):
        bun_name = create_bun.get_name()
        assert bun_name == DataBun.BUN_NAME

    def test_get_bun_price(self, create_bun):
        bun_price = create_bun.get_price()
        assert bun_price == DataBun.BUN_PRICE