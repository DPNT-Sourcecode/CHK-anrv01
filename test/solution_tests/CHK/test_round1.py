from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_read_functionality(self):
        input_skus = "ABCDADC"
        total_value = checkout(input_skus)
        assert total_value == 200

    def test_bad_input(self):
        input_skus = 400
        total_value = checkout(input_skus)
        assert total_value == -1
