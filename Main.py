# ------------------------------------------------------------------------ #
# Title: Assignment09 Main.py
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 09
# NDaharia,6.16.2022,Modified code to complete assignment 09
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    import DataClasses as DC  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body. Done.
lstEmployees = []  # list of lists
strFile = "EmployeeData.txt"
strChoice = ""
strStatus = ""
lstObjects = [] # list of employee objects

# Load data from file into a list of employee objects when script starts
try:
    lstEmployees = P.FileProcessor.read_data_from_file(strFile)
    for item in lstEmployees:
        emp_obj = DC.Employee(item[0], item[1], item[2].strip())  # reconfiguring list into objects
        lstObjects.append(emp_obj)

except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')

    # Show user a menu of options
while True:
    IO.EmployeeIO.print_menu_items()

# Get user's menu option choice
    strChoice = IO.EmployeeIO.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == "1":
        IO.EmployeeIO.print_current_list_items(lstObjects)
        continue

    # Let user add data to the list of employee objects
    elif strChoice == "2":
        try:
            emp_data = IO.EmployeeIO.input_employee_data()
            print(emp_data, type(emp_data))
            lstObjects.append(emp_data)
        except Exception as e:
            print(e, e.__doc__, type(e))
        continue

    # let user save current data to file
    elif strChoice == "3":
        strStatus = P.FileProcessor.save_data_to_file(strFile, lstObjects)
        if strStatus == True:
            print("Data Save Success!")
        else:
            print("Data NOT Saved.")
        continue

    # Let user exit program
    elif strChoice == "4":
        print("Exiting program.")
        break

    else:
        print("Please only choose 1, 2, 3, or 4!")
# Main Body of Script  ---------------------------------------------------- #
