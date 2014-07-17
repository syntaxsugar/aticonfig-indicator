import unittest
from aticonfig_indicator import utils

ATICONFIG_OUTPUT = """
    Adapter 0 - AMD Mobility Radeon HD 5000 Series
            Sensor 0: Temperature - 68.00 C"""


class UtilsTestCase(unittest.TestCase):
    def test_call(self):
        self.assertNotEqual(0, utils.get_aticonfig_output())

    def test_parse_aticonfig(self):
        self.assertEqual('68.00', utils.parse_aticonfig(ATICONFIG_OUTPUT))

    def test_live(self):
        self.assertIsNotNone(utils.get_temp())


if __name__ == '__main__':
    unittest.main()
