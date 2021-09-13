from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_read_functionality(self):
        input_skus = "A B CDAD,C"
        total_value = checkout(input_skus)
        assert total_value == 