import country_name_and_year 


def testmauritius():
    assert "Summer" == country_name_and_year.mauritius(3), "10< month <13 or 1 <= month <=4"
    assert "Autumn" == country_name_and_year.mauritius(5), "month = 5"
    assert "Winter" == country_name_and_year.mauritius(7), "5 <month < 10"
    assert "Spring" == country_name_and_year.mauritius(10), "month =10"


if __name__ == "__main__":
    testmauritius()


