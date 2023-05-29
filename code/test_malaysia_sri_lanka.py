import country_name_and_year 
import unittest  

class malaysia_sri_lanka_test(unittest.TestCase):
    def testMalaysia_sri_lanka(self):
        self.assertEqual( "Northeast Monsoon" , country_name_and_year.malaysia_sri_lanka(1), "Month = 12 or month = 1 or month = 2")
        self.assertEqual( "Inter-monsoon" , country_name_and_year.malaysia_sri_lanka(3), "month = 3 or month = 4")
        self.assertEqual( "Southeast Monsoon" , country_name_and_year.malaysia_sri_lanka(8), "5<=month<= 9")
        self.assertEqual( "Inter-monsoon" , country_name_and_year.malaysia_sri_lanka(10), "month = 10 or month = 11")


