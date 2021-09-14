from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_k_functionality(self):
        input_skus = "KK"
        total_value = checkout(input_skus)
        assert total_value == 150

    def test_n_functionality(self):
        input_skus = "NNNM"
        total_value = checkout(input_skus)
        assert total_value == 120

    def test_p_functionality(self):
        input_skus = "PPPPP"
        total_value = checkout(input_skus)
        assert total_value == 200

    def test_q_functionality(self):
        input_skus = "QQQQQQ"
        total_value = checkout(input_skus)
        assert total_value == 160

    def test_r_functionality(self):
        input_skus = "RRRQ"
        total_value = checkout(input_skus)
        assert total_value == 150

    def test_u_functionality(self):
        input_skus = "UUUU"
        total_value = checkout(input_skus)
        assert total_value == 120

    def test_v_functionality(self):
        input_skus = "VVV"
        total_value = checkout(input_skus)
        assert total_value == 130
