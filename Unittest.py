import unittest

class TestCalculator(unittest.TestCase):

	def test_cinco_mas_cinco_igual_diez(self):
		assert 5 + 5 == 10

	def test_cinco_por_cinco(self):
		assert 5 * 5 == 25

if __name__ == "__main__":
	unittest.main()
