def Detector(location,time,temp):
    if location == 0 :
        if time == "M":
            if temp > 18.2 :
                print("The temperature is greater than the average this morning in Perth")
                if temp-18.2 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C")
            else: 
                print("The temperature is below average this morning in Perth")
                if 18.2-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C")
        else:
            if temp > 23.0 :
                print("The temperature is greater than the average this afternoon in Perth")
                if temp-23.0 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C")
            else: 
                print("The temperature is below average this afternoon in Perth")
                if 23.0-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C")
    else:
        if time == "M":
            if temp > 16.5 :
                print("The temperature is greater than the average this morning in Adelaide")
                if temp-16.5 > 5.0:
                    print("The difference from the mean temperature is more than 5.0 C")
            else: 
                print("The temperature is below average this morning in Adelaide")
                if 16.5-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C")
        else:
            if temp > 21.0 :
                print("The temperature is greater than the average this afternoon in Adelaide")
                if temp-21.0 >5.0:
                    print("The difference from the mean temperature is more than 5.0 C")
            else: 
                print("The temperature is below average this afternoon in Adelaide")
                if 21.0-temp >5.0:
                    print("The difference from the mean temperature is above 5.0 C")
if __name__ == '__main__':
    
    loc = int(input('Enter your location(0,1):  '))
    M_A = input("Enter the time of the day(M/A):  ").upper()
    temp = float(input('Enter the temperature:   '))

    Detector(loc,M_A, temp)


            

            
                  
