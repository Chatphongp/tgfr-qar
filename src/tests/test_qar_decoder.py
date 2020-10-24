import unittest
import qar_decoder as qd


class TestTwoComplements(unittest.TestCase):
    def _get_int_from_binary_str(self, bin_val):
        return int(bin_val, 2)

    def test_two_complements_negative_value(self):
        val = self._get_int_from_binary_str("10000000")
        result = qd.twos_complement(val, 8)
        self.assertEqual(result, -128)

    def test_two_complements_positive_value(self):
        val = self._get_int_from_binary_str("01111111")
        result = qd.twos_complement(val, 8)
        self.assertEqual(result, 127)
