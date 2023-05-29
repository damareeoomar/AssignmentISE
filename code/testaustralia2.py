import country_name_and_year 
import unittest  

class Australia_2_test(unittest.TestCase):
    def testaustralia_2(self):
        self.assertEqual( "Birak" , country_name_and_year.australia_2(1), "Month = 12 or month = 1")
        self.assertEqual( "Bunuru" , country_name_and_year.australia_2(2), "Month = 2 or month = 3")
        self.assertEqual( "Djeran" , country_name_and_year.australia_2(4), "Month = 4 or month = 5")
        self.assertEqual( "Makuru" , country_name_and_year.australia_2(6), "Month = 6 or month = 7")
        self.assertEqual( "Djilba" , country_name_and_year.australia_2(8), "Month = 8 or month = 9")
        self.assertEqual( "Kambarang" , country_name_and_year.australia_2(10), "Month = 10 or month = 11")




