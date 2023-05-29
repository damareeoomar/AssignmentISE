import country_name_and_year 


def testaustralia_1():
    assert "Summer" == country_name_and_year.australia_1(12), "month = 12 or month =1 or month =2 "
    assert "Autumn" == country_name_and_year.australia_1(5), "2< month <6"
    assert "Winter" == country_name_and_year.australia_1(7), "5 <month < 9"
    assert "Spring" == country_name_and_year.australia_1(10), "8< month < 12"


if __name__ == "__main__":
    testaustralia_1()