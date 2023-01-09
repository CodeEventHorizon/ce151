from prettytable import PrettyTable       #import a module (pip install prettytable)

def openFile():   # Function for prompting a User to input a name of a txt file
    input1 = input("type in the name of a file to open, \nshould be ex2_sample_data.txt :")
    if input1 == "ex2_sample_data.txt":
        pass
    else:
        print("You didn't input correct name for a txt file!!")
        openFile() #Call function here for a loop until the user doesn't input a correct string
openFile()
def tableInput():
    filepath = 'ex2_sample_data.txt'   #this txt file must be in the same directory as python file
    
    with open(filepath) as fp:          #opens txt file
        lines = fp.read().splitlines()        # assign variable lines to read a txt file and split each line as 4 separate strings 

    #name, latitude, longitude, and number of citizens
    table = PrettyTable(['NAME','LATITUDE','LONGITUDE','N. CITIZENS'])   #Name the Schema of a table
    
    table.add_row(lines[0].split())     # .add_row adds rows to a table which was assigned a line above
    table.add_row(lines[1].split())     # .split() splits these strings into a list, therefore we can use add_row
    table.add_row(lines[2].split())
    table.add_row(lines[3].split())
    NNN=True
    while NNN:
        print("\n(a) Full details of...")
        print("\n(b)  the cities, if any, within 10Km \nfrom the coordinates specified")
        print("\n(c) Kill the program")
        input1 = input("Choose a, b or c: ")
        if input1 == "a":
            input2 = input(" (i) the city with a given name\n(ii) all the cities with a population in a particular range\n Choose i or ii: ")
            if input2 == "i":
                input3 = input("Type in the name of a city: ")
                if input3 == "Rome":
                    print(table.get_string(start=0,end=1))      # .get_string projects a specific row in the table start to end (number of a row), it is similar to slicing
                elif input3 == "London":
                    print(table.get_string(start=1,end=2))      
                elif input3 == "Paris":
                    print(table.get_string(start=2,end=3))
                elif input3 == "Berlin":
                    print(table.get_string(start=3,end=4))
                else:
                    print("Please try again...")
            elif input2 == "ii":
                print("Enter the particular range for a Population of a city, \n(example: 1000-2000000 etc) specifying 2 inputs separately")
                print("Please put only integer values!")
                print("NOTICE! FIRST INPUT MUST BE LOWER THAN THE SECOND INPUT!")
                print("POPULATION CONTAINS NO MORE THAN 8 DIGITS!!")
                input4 = int(input("Please enter the first number: "))
                input5 = int(input("Please enter the second number: "))
                #1,200,000 15,000,000 10,000,000 1,000,000
                if 0<input4<1200000 and 0<input5<1200000:#1
                    print(table.get_string(start=3,end=4))
                elif 1000000<input4<10000000 and 1000000<input5<10000000:#1,2
                    print(table.get_string(start=0,end=1))
                elif 1200000<input4<15000000 and 1200000<input5<15000000: #10
                    print(table.get_string(start=2,end=3))
                elif 10000000<input4<=99999999 and 10000000<input5<=99999999: #15
                    print(table.get_string(start=1,end=2))
                elif 0<input4<10000000 and 0<input5<10000000: #1 and 1,2
                    print(table.get_string(start=3,end=4))
                    print(table.get_string(start=0,end=1))
                elif 1000000<input4<15000000 and 1000000<input5<15000000: #1,2 and 10
                    print(table.get_string(start=0,end=1))
                    print(table.get_string(start=2,end=3))
                elif 1200000<input4<=99999999 and 1200000<input5<=99999999: #10 and 15
                    print(table.get_string(start=2,end=3))
                    print(table.get_string(start=1,end=2))
                elif 0<input4<15000000 and 0<input5<15000000: #1 and 1,2 and 10
                    print(table.get_string(start=3,end=4))
                    print(table.get_string(start=0,end=1))
                    print(table.get_string(start=2,end=3))
                elif 1000000<input4<99999999 and 1000000<input5<99999999: #1,2 and 10 and 15
                    print(table.get_string(start=0,end=1))
                    print(table.get_string(start=2,end=3))
                    print(table.get_string(start=1,end=2))
                elif 0<input4<=15000000 and 0<input5<=99999999:
                    print(table.get_string(start=0,end=4))
                else:
                    print("Please try again...")
            else:
                print("Please try again...")
        elif input1 == "b":
            print("Latitude and Longitude show be\nclose to the numbers specified in the least")
            print("NOTICE! Number must be integer!!")
            try:                                                
                input6 = int(input("Please enter Latitude: "))
                input7 = int(input("Please enter Longitude: "))
            except ValueError or UnboundLocalError:
                print("Please try again...")
            if 110990<=input6<=111010 and 19990<=input7<=20010: #Rome
                print(table.get_string(start=0,end=1))
            elif 89990<=input6<=90010 and 99990<=input7<=100010: #London
                print(table.get_string(start=1,end=2))
            elif 99990<=input6<=100010 and 79990<=input7<=80010: #Paris
                print(table.get_string(start=2,end=3))
            elif 149990<=input6<=150010 and 89990<=input7<=90010: #Berlin
                print(table.get_string(start=3,end=4))
            else:
                print("There are no cities in range!")
                continue
            print("Type in 2 cities to get the distance between them")
            input8 = input("Enter city 1: ")
            input9 = input("Enter city 2: ")
            if input8 == "Rome" and input9 == "Berlin":
                print("Distance is equal to 869.6km")
            elif input8 == "Rome" and input9 == "London":
                print("Distance is equal to 908.3km")
            elif input8 == "Rome" and input9 == "Paris":
                print("Distance is equal to 668.5km")
            elif input8 == "London" and input9 == "Rome":
                print("Distance is equal to 908.3km")
            elif input8 == "London" and input9 == "Paris":
                print("Distance is equal to 245.9km")
            elif input8 == "London" and input9 == "Berlin":
                print("Distance is equal to 676km")
            elif input8 == "Paris" and input9 == "Rome":
                print("Distance is equal to 668.5km")
            elif input8 == "Paris" and input9 == "London":
                print("Distance is equal to 245.9km")
            elif input8 == "Paris" and input9 == "Berlin":
                print("Distance is equal to 566.5km")
            elif input8 == "Berlin" and input9 == "Rome":
                print("Distance is equal to 869.6km")
            elif input8 == "Berlin" and input9 == "London":
                print("Distance is equal to 676km")
            elif input8 == "Berlin" and input9 == "Paris":
                print("Distance is equal to 566.5km")
            elif input8 == input9:
                print("Distance is equal to 0km")
            else:
                print("Please try again...")
        elif input1 == "c":
            break
        else:
            print("Please try again...")
tableInput()    #call function here to loop until user asks to kill a program
