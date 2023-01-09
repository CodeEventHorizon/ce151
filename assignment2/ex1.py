from prettytable import PrettyTable    #import a module (pip install prettytable)

def tableInput():
    filepath = 'ex1_sample_data.txt' #this txt file must be in the same directory as python file
    with open(filepath) as fp:
        lines = fp.read().splitlines()

    myorder = [3,2,4,1,0]   # create a new list to re-order the position of columns in the txt file
    table = PrettyTable(['LAST-NAME','FIRST-NAME','SALARY','POSITION','TEAM'])

    first = lines[0].split()   #turn the first line into a string
    first = [first[i] for i in myorder]    #re-order

    second = lines[1].split()
    second = [second[i] for i in myorder]

    third = lines[2].split()
    third = [third[i] for i in myorder]

    fourth = lines[3].split()
    fourth = [fourth[i] for i in myorder]

    table.add_row(first)
    table.add_row(second)
    table.add_row(third)
    table.add_row(fourth)
    NNN=True
    while NNN:
        print("\n(a) Full details of the player...")
        print("\n(b) The first- and last- names of all players of a team")
        print("\n(c) Kill the program")
        input1 = input("\nChoose a, b or c: ")
        if input1 == "a":
            print("\n(i) The player with a given last-name: ")
            print("\n(ii) All players with a salary in a particular range")
            input2 = input("\nChoose i or ii: ")
            if input2 == "i":
                input3 = str(input("Type in the last-name of a player: "))
                if input3 == "Green":
                    print(table.get_string(start=0,end=1))  # .get_string projects a specific row in the table start to end (number of a row), it is similar to slicing   
                elif input3 == "Zappacosta":
                    print(table.get_string(start=1,end=2))
                elif input3 == "Lacazette":
                    print(table.get_string(start=2,end=3))
                elif input3 == "Mkhitaryan":
                    print(table.get_string(start=3,end=4))
                else:
                    print("\nThere is no such player in a Table")
            elif input2 == "ii":
                print("Enter the particular range for a salary, (example: 1000-2000000 etc) specifying 2 inputs separately")
                print("Please put only integer values!")
                print("NOTICE! FIRST INPUT MUST BE LOWER THAN THE SECOND INPUT!")
                print("SALARY CONTAINS NO MORE THAN 8 DIGITS")
                input4 = int(input("Please enter the first number: "))
                input5 = int(input("Please enter the second number: "))
                #0:10mil, 1:20mil, 2:30mil, 3:15mil
                if 0<=input4<=10000000 and 0<input5<=14999999:  #10,000,000
                    print(table.get_string(start=0,end=1))
                elif 10000000<input4<20000000 and 10000000<input5<20000000: #15,000,000
                    print(table.get_string(start=3,end=4))
                elif 15000000<input4<30000000 and 15000000<input5<30000000: #20,000,000
                    print(table.get_string(start=1,end=2))
                elif 20000000<input4<30000000 and 20000000<input5<99999999: #30,000,000
                    print(table.get_string(start=2,end=3))
                elif 0<=input4<=15000000 and 0<input5<=19999999:#10,000,000 and 15,000,000
                    print(table.get_string(start=0,end=1))
                    print(table.get_string(start=3,end=4))
                elif 10000000<input4<20000000 and 10000000<input5<30000000:#15,000,000 and 20,000,000
                    print(table.get_string(start=3,end=4))
                    print(table.get_string(start=1,end=2))
                elif 15000000<input4<=30000000 and 15000000<input5<=99999999:#20,000,000 and 30,000,000
                    print(table.get_string(start=1,end=3))
                elif 0<=input4<29999999 and 0<input5<=29999999:#10,000,000 and 15,000,000 and 20,000,000
                    print(table.get_string(start=3,end=4))
                    print(table.get_string(start=0,end=2))
                elif 10000000<input4<=30000000 and 10000000<input5<=99999999:#15,000,000 and 20,000,000 and 30,000,000
                    print(table.get_string(start=1,end=4))    
                elif 0<input4<=30000000 and 0<input5<=99999999:
                    print(table)
                else:
                    print("\nNo Player has such salary in the table!")
            else:
                print("\nPlease try again...")
        elif input1 == "b":
            print("Description: Both FIRST-NAME and LAST-NAME must \n\tstart with a capital letter (Example: Robert Green)")
            input6 = input("Please enter First- and Last- name of a player\n(ORDER: FIRST-NAME, LAST-NAME): ")
            if input6 == "Robert Green":
                print(table.get_string(start=0,end=1))
            elif input6 == "Davide Zappacosta":
                print(table.get_string(start=1,end=2))
            elif input6 == "Alexandre Lacazette":
                print(table.get_string(start=2,end=3))
            elif input6 == "Henrikh Mkhitaryan":
                print(table.get_string(start=3,end=4))
            else:
                print("\nPlease try again...")
        elif input1 == "c":
            break
        else:
            print("\nPlease try again...")

tableInput() #call function here for a loop until a user asks to kill a program
