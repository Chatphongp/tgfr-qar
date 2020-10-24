import unittest
import numpy as np
from src import qar_decoder as qd


class TestTwoComplements(unittest.TestCase):
    def test_two_complements(self):
        val = int("10000000", 2)
        result = qd.twos_complement(val, 8)
        self.assertEqual(result, -128)
