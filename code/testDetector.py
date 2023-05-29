import mean_temperature
import unittest , sys , io , os 

class Detector_test(unittest.TestCase) :
    def testDetector(self):
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 18.2)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is equal to the average.\n",actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 20.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Perth.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 28.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Perth.\n\nThe difference from the mean temperature is more than 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 47.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Perth.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 16.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Perth.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 10.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Perth.\n\nThe difference from the mean temperature is above 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'M', 0.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Perth.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 23.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is equal to the average.\n",actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 25.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Perth.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 29.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Perth.\n\nThe difference from the mean temperature is more than 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 48.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Perth.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 22.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Perth.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', 17.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Perth.\n\nThe difference from the mean temperature is above 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("perth", 'A', -1.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Perth.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        
        
        
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 16.5)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is equal to the average.\n",actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 18.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Adelaide.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 22.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Adelaide.\n\nThe difference from the mean temperature is more than 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 50.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this morning in Adelaide.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 16.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Adelaide.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', 3.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Adelaide.\n\nThe difference from the mean temperature is above 5.0 C\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'M', -2.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this morning in Adelaide.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 21.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is equal to the average.\n",actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 23.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Adelaide.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 35.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Adelaide.\n\nThe difference from the mean temperature is more than 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 55.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is greater than the average this afternoon in Adelaide.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 19.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Adelaide.\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', 14.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Adelaide.\n\nThe difference from the mean temperature is above 5.0 C\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        capOut = io.StringIO()
        sys.stdout = capOut 
        mean_temperature.Detector("adelaide", 'A', -5.0)
        actual = capOut.getvalue()
        self.assertEqual("The temperature is below average this afternoon in Adelaide.\n\nThe difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n\n"
,actual)
        sys.stout = sys.__stdout__
        
        
        