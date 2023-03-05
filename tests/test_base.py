import unittest

from gramTrade import clean_values, find_pair, retrieve_position, find_values, order_type


class GramTradeFunctions(unittest.TestCase):

    def test_clean_value_1(self):
        value1 = clean_values(" 1,085 ")
        result1 = "1.085"
        self.assertEqual(value1, result1)

    def test_clean_value_2(self):
        value2 = clean_values(" 1.085")
        result2 = "1.085"
        self.assertEqual(value2, result2)

    def test_clean_value_3(self):
        value3 = clean_values("1,085 ")
        result3 = "1.085"
        self.assertEqual(value3, result3)

    def test_clean_value_4(self):
        value3 = clean_values(" 10850 ")
        result3 = "10850"
        self.assertEqual(value3, result3)

    def test_find_pairs_ok(self):
        pair = find_pair("XAUUSD - Time Frame M5 ")
        result = "XAUUSD"
        self.assertEqual(pair, result)

    def test_find_pairs_none(self):
        pair = find_pair("XAUXAU - Time Frame M5 ")
        self.assertIsNone(pair)

    def test_retrieve_position_buy(self):
        tps = ["1.7627", "1.7827"]
        sl = "1.7244"
        position = retrieve_position(sl, tps)
        result = "BUY"
        self.assertEqual(result, position)

    def test_retrieve_position_short(self):
        tps = ["1.7244", "1.7100"]
        sl = "1.7627"
        position = retrieve_position(sl, tps)
        result = "SELL"
        self.assertEqual(result, position)

    def test_find_value(self):
        values = "TP1: 1.57100"
        value = find_values(values)
        result = "1.57100"
        self.assertEqual(result, value)

    def test_find_value_2(self):
        values = "TP1: 1,5710"
        value = find_values(values)
        result = "1.5710"
        self.assertEqual(result, value)

    def test_find_value_3(self):
        values = "SL: 1780"
        value = find_values(values)
        result = "1780"
        self.assertEqual(result, value)

    def test_find_value_none(self):
        values = "pas de data"
        value = find_values(values)
        self.assertIsNone(value)

    def test_order_type_buy(self):
        values = "🔴 BUY EURAUD"
        expected = "BUY"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_long(self):
        values = "TRADE eifnezlnfef long EURAUD"
        expected = "BUY"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_achat(self):
        values = "achat EURAUD"
        expected = "BUY"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_SELL(self):
        values = "🔴 SELL EURAUD"
        expected = "SELL"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_SELL_LIMIT(self):
        values = "🔴 SELL limit EURAUD"
        expected = "SELL LIMIT"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_short(self):
        values = "short EURAUD"
        expected = "SELL"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_vente(self):
        values = "vente EURAUD"
        expected = "SELL"
        result = order_type(values)
        self.assertEqual(expected, result)

    def test_order_type_none(self):
        values = "shortvente EURAUD"
        result = order_type(values)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
