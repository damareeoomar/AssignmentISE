import country_name_and_year
import unittest , sys , io ,os 



class NameMonthTesst(unittest.TestCase):
    def testNameMonth(self):
    
        sys.stdin = io.StringIO("Damaree\n12\n")
        capOut = io.StringIO()
        sys.stdout = capOut 

        country_name_and_year.Name_Month()

        actual = capOut.getvalue()
        self.assertEqual("Enter the country name: Enter the number of the month of the year:(1-12) DAMAREE   12\n"
,actual)
        sys.stdin = sys.__stdin__
        sys.stout = sys.__stdout__
        
        sys.stdin = io.StringIO("Dubai\n4419\n2")
        capOut = io.StringIO()
        sys.stdout = capOut 

        country_name_and_year.Name_Month()

        actual = capOut.getvalue()
        self.assertEqual("Enter the country name: Enter the number of the month of the year:(1-12) Wrong input of month number. Try again (1 -12) DUBAI   2\n"

,actual)
        sys.stdin = sys.__stdin__
        sys.stout = sys.__stdout__
