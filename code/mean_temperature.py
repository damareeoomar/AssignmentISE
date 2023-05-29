# Student Name: Damaree Muhammad Oomar Farook 
# Student ID: 21564419
#
#
#
def choice(input1,list1,error,message):
    while input1 not in list1 :
        print(error)
        input1 = input(message)
    return input1


def InputFile(name):
    file = open(name)
    count = 1  
    for line in file:
        z = line.strip().split(",")
        print("LINE NUMBER IN DATA FILE IS", count,'\n')
        Detector(z[0].lower(), z[1][0].upper(), float(z[2]))
        count +=1
    file.close()
    
def Detector(location,time,temp):
    if location == "perth" :
        if time == "M":
            if temp != 18.2:
                if temp > 18.2 :
                     print("The temperature is greater than the average this morning in Perth.\n")
                
                     if temp-18.2 >5.0 and temp < 46.0:
                        print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                     elif temp-18.2 >5.0 and temp > 46.0:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                
                else: 
                    print("The temperature is below average this morning in Perth.\n")
                
                    if 18.2-temp >5.0 and temp > 0.7:
                        print("The difference from the mean temperature is above 5.0 C\n\n")
                    
                    elif 18.2-temp >5.0 and temp < 0.7:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
            else:
                print("The temperature is equal to the average.")      
                
        else:
            if temp != 23.0:
                if temp > 23.0 :
                    print("The temperature is greater than the average this afternoon in Perth.\n")
                
                    if temp-23.0 >5.0 and temp < 46.0 :
                        print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                    elif temp-23.0 >5.0 and temp > 46.0 :
                        print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                    
                
                else: 
                    print("The temperature is below average this afternoon in Perth.\n")
                
                    if 23.0-temp >5.0 and temp >0.7:
                        print("The difference from the mean temperature is above 5.0 C\n\n")
                    
                    elif 23.0-temp >5.0 and temp < 0.7 :
                        print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
            else:
                print("The temperature is equal to the average.")       
                
    else:
        if time == "M":
            if temp != 16.5:

                if temp > 16.5 :
                     print("The temperature is greater than the average this morning in Adelaide.\n")
                
                     if temp-16.5 > 5.0 and temp < 49.0:
                        print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                     elif temp-16.5 > 5.0 and temp > 49.0:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")
                    
                
                else: 
                    print("The temperature is below average this morning in Adelaide.\n")
                
                    if 16.5-temp >5.0 and temp >-1.0:
                        print("The difference from the mean temperature is above 5.0 C\n")
                    
                    elif 16.5-temp >5.0 and temp <-1.0:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
            else: 
                 print("The temperature is equal to the average.")     
                
        else: 
            if temp != 21.0:
                if temp > 21.0 :
                    print("The temperature is greater than the average this afternoon in Adelaide.\n")
                
                    if temp-21.0 >5.0 and temp < 49.0:
                        print("The difference from the mean temperature is more than 5.0 C\n\n")
                    
                    elif temp-21.0 >5.0 and temp > 49.0:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  above the maxmimum temperature in this area.\n\n")

                else: 
                    print("The temperature is below average this afternoon in Adelaide.\n")
                
                    if 21.0-temp >5.0 and temp > -1.0:
                        print("The difference from the mean temperature is above 5.0 C\n\n")
                    elif 21.0-temp >5.0 and temp < -1.0:
                        print("The difference between the mean is greater than 5.0 C and the temperature is  below the minimum temperature in this area.\n\n")
            else:
                print("The temperature is equal to the average.")
if __name__ == '__main__':
    
    choice_input = input('Do you want to input data manually(1) or do you want to import data from a file(2):  ')
    choice_input = choice(choice_input,["1","2"],"Wrong input","Choose between \'1\' or \'2\': ")
    if choice_input == "2":
        name = input("Enter File name: ")
        InputFile(name)
    else:
        location = (input('Enter your location( \'perth\'for Perth or \'adelaide\' for Adelaide):  ')).lower()
        location = choice(location,["perth", "adelaide"], "Location current not present in our systems.","Choose among the available ones :")
        time = input("\nEnter the time of the day(M/A):  ").upper()
        time = choice(time, ["A","M"],"Wrong input.", "Please choose between (A)fternoon or (M)orning: ")
        temp = float(input('\nEnter the temperature:   '))

        Detector(location,time, temp)
   

   
            
   
            
                  
