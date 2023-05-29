# Student Name: Damaree Muhammad Oomar Farook 
# Student ID: 21564419
#
#
#
    
def Detector(location,time,temp):
    if location == "perth" :
        if time == "M":
            if temp > 18.2 :
                print("The temperature is greater than the average this morning in Perth.\n")
                
                if temp-18.2 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                elif temp-18.2 >5.0 and temp > 46.0:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                
            else: 
                print("The temperature is below average this morning in Perth.\n")
                
                if 18.2-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C\n\n")
                    
                elif 18.2-temp >5.0 and temp < 0.7:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
                    
                
        else:
            if temp > 23.0 :
                print("The temperature is greater than the average this afternoon in Perth.\n")
                
                if temp-23.0 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                elif temp-23.0 >5.0 and temp > 46.0 :
                    print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                    
                
            else: 
                print("The temperature is below average this afternoon in Perth.\n")
                
                if 23.0-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C\n\n")
                    
                elif 23.0-temp >5.0 and temp < 0.7 :
                    print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
                    
                
    else:
        if time == "M":
            if temp > 16.5 :
                print("The temperature is greater than the average this morning in Adelaide.\n")
                
                if temp-16.5 > 5.0:
                    print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                elif temp-16.5 > 5.0 and temp > 49.0:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                    
                
            else: 
                print("The temperature is below average this morning in Adelaide.\n")
                
                if 16.5-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C\n")
                    
                elif 16.5-temp >5.0 and temp <-1.0:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
                   
                
        else:
            if temp > 21.0 :
                print("The temperature is greater than the average this afternoon in Adelaide.\n")
                
                if temp-21.0 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                elif temp-21.0 >5.0 and temp > 49.0:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                    
                
            else: 
                print("The temperature is below average this afternoon in Adelaide.\n")
                
                if 21.0-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C\n\n")
                elif 21.0-temp >5.0 and temp < -1.0:
                    print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
if __name__ == '__main__':
    
    loc = int(input('Enter your location(0,1):  '))
    M_A = input("Enter the time of the day(M/A):  ").upper()
    temp = float(input('Enter the temperature:   '))

    Detector(loc,M_A, temp)

   
            
   
            
                  
