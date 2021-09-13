from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_read_functionality(self):
        input_skus = "A B CDAD,C"
        total_value = checkout(input_skus)
        assert total_value == 200

    def test_bad_input(self):
        input_skus = 400
        total_value = checkout(input_skus)
        assert total_value == -1

    def test_special_offer(self):
        input_skus = "AABA, B"
        total_value = checkout(input_skus)
        assert total_value == 175
