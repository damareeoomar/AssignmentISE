#
# 
#

def Name_Month():
    global country, month, season
    a = input("Enter the country name: ")        
    country = a.upper()
    
    b = input("Enter the number of the month of the year:(1-12) ")   
    month = int(b)
    print(country, " ", month)
 
 
def season1(country,month):
    if country == "AUSTRALIA":
        if month == 12 or 0<month<3 :
            season = "Summer"
        elif 2 < month < 6 :
            season = "Autumn"
        elif 5 < month < 9:
            season = "Winter"
        else:
            season = "Spring"
    elif country == 'MAURITUS':
        if 10 < month < 13   or 0 < month < 5:
            season = "Summer"
        elif month== 5 :
            season = "Autumn"
        elif 5 < month < 10:
            season = "Spring"
        else:
            season = "Winter"
    elif country =="SPAIN":
        if month == 12 or 0 <month<3 :
            season = "Winter"
        elif 2 < month < 6 :
            season = "Spring"
        elif 5 < month < 9:
            season = "Summer"
        else:
            season = "Autumn"
    else:
        if 11 < month < 3:
            season = "Northeast Monsoon"
        elif 4 < month < 10:
            season = "Southeast Monsoon"
        else:
            season = "Inter-monsoon"
    return season 
        





if __name__ == "__main__":
    Name_Month()
    

    season2 = season1(country,month)
    print(season2)
