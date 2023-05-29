#
# 
#
import matplotlib.pyplot as plt
import matplotlib.image as im 





def Name_Month():
    global country, month
    a = input("Enter the country name: ")        #a = input("Enter the country name: ").upper()
    country = a.upper()
    
    b = input("Enter the number of the month of the year:(1-12) ")   
    month = int(b)
    while month not in range(1,13):
        b = input("Wrong input of month number. Try again (1 -12) ")
        month = int(b)
    print(country," ",month)


def mauritius(month):
    if 10 < month < 13   or 0 < month < 5:
        season = "Summer"
    elif month == 5 :
        season = "Autumn"
    elif 5 < month < 10:
        season = "Winter"
    else:
        season = "Spring"
        
    return season


def spain_japan(month):
    if month == 12 or 0 <month<3 :
        season = "Winter"
    elif 2 < month < 6 :
        season = "Spring"
    elif 5 < month < 9:
        season = "Summer"
    else:
        season = "Autumn"
        
    return season


def australia_2(month):
     if month == 12 or month ==1 :
         season = "Birak"
     elif month == 2 or month ==3 :
         season = "Bunuru"
     elif month == 4 or month == 5 :
         season = "Djeran"
     elif month == 6 or month == 7 :
         season = "Makuru"
     elif month == 8 or month == 9 :
         season = "Djilba"
     else:
         season = "Kambarang"
    
     return season
 
         
def australia_1(month):
    if month == 12 or 0<month<3 :
        season = "Summer"
    elif 2 < month < 6 :
        season = "Autumn"
    elif 5 < month < 9:
        season = "Winter"
    else:
        season = "Spring"
        
    return season


def malaysia_sri_lanka(month):
        if month == 12 or month < 3:
            season = "Northeast Monsoon"
        elif 4 < month < 10:
            season = "Southeast Monsoon"
        else:
            season = "Inter-monsoon"
            
        return season
    
    
def location(country,month):
    if country == "AUSTRALIA":
        choice = int(input("Do you want The traditional seasons(1) or the Noongar Seasons(2):  "))
        if choice == 1 :
            season = australia_1(month)
        else:
            season = australia_2(month)
    elif country == 'MAURITIUS':
        season = mauritius(month)
        
    elif country =="SPAIN" or  country =="JAPAN":
        season = spain_japan(month)
    elif country == "SRI LANKA" or country == "MALAYSIA":
        season = malaysia_sri_lanka(month)
    else:
        season = "Wrong"
 
    return season 
    
    
def image(season):
    
    plt.imshow(im.imread(season.lower()+".png"))
    plt.title(country +" & "+ season.upper(), fontsize = "17")
    
    plt.show()



if __name__ == "__main__":

    
    Name_Month()
  

    season = location(country,month)
    image(season)
    print(season)
