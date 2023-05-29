import country_name_and_year
import unittest , sys , io ,os 



class LocationTest(unittest.TestCase):
    def testLocation(self): 
        
        sys.stdin = io.StringIO("1\n")
        actual = country_name_and_year.location("AUSTRALIA", 1)
        self.assertEqual("Summer", actual)

        
        sys.stdin = sys.__stdin__
        
        sys.stdin = io.StringIO("2\n")
        actual = country_name_and_year.location("AUSTRALIA", 1)
        self.assertEqual("Birak", actual)

        
        
        

