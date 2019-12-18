with open('read file data.txt', 'r') as file:
    text = file.readlines()
    print(text)
IDlist = ['S0001','S0002','S0003','S0004','S0005','S0006','S0007','S0008','S0009','S0010']
Namelist = ['Garry','James','Yuli','Judith','Budi','Toni','Andy','Brad','Diana','David']
def display_records():
    print("|ID      |Name       |Position       |Salary     |")
    print(IDlist+"\n")

menu_chosen = input("Input Choice: ")
def new_staff():
    while True:
        if menu_chosen == 1:
            print("New Staff")
            input_staff_id = input("Input ID[SXXXX]: ")
            if len(input_staff_id) == 5 and input_staff_id[0] == "S" and input_staff_id[1:6].isdigit():
                input_staff_name = input("Input Name[0...20]: ")
                if len(input_staff_name) <= 20:
                    input_staff_position = input("Input Position[Staff|Officer|Manager]: ")
                    if input_staff_position == "Staff"
                        input_salary_staff = input("Input Salary: ")
                        if input_salary_staff >= 3500000 and input_salary_staff <= 7000000:
                            print("Staff Salary: ", input_salary_staff)
                    elif input_staff_position == "Officer":
                        input_salary_officer = input("Input Salary: ")
                        if input_salary_officer > 7000000 and input_salary_officer <= 10000000:
                            print("Officer Salary: ", input_salary_officer)
                    elif input_staff_position == "Manager":
                        input_salary_manager = input("Input Salary: ")
                        if input_salary_manager > 10000000:
                            print("Manager Salary: ", input_salary_manager)

            else:
                print("Error input")
                break
        break

def delete_staff():
    while True:
        input_staff_id = input("Input Staff ID: ")


