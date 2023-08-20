import unittest

import HtmlTestRunner

from Test_eMAG import Test


class TestSuite(unittest.TestCase):

		def test_suite(self):
				teste_de_rulat = unittest.TestSuite()
				teste_de_rulat.addTests([#unittest.defaultTestLoader.loadTestsFromTestCase(Elefant_Login),
																 unittest.defaultTestLoader.loadTestsFromTestCase(Test)])

				runner = HtmlTestRunner.HTMLTestRunner\
								(
				combine_reports=True, # daca rulam mai multe clase, ne va genera raport
				report_title = "Test execution report",
				report_name = "Test results"
		)

				runner.run(teste_de_rulat)