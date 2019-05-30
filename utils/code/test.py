import unittest

import datautils



class TestUtils(unittest.TestCase):

	def test_load_csv(self):
		df = datautils.load_csv(2018)
		self.assertEqual(len(df), 2619968)




	def main():
		self.test_load_csv()


if __name__ == '__main__':
    unittest.main()