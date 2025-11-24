import os


os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("==========================")

#Empty dictionary
student_record = {}

while True: 
    print("Select From The Following Options")
    print("A - Add student record")
    print("B - Print all student record")
    print("C - Search student record")
    print("D - Delete student record")
    print("E - Edit student record")
    print("F - Export student Record")
    print("G - Exit Sytem")

    choice = input("Select From The Options Above --->").lower()

    if choice == 'a':
        os.system('cls')
        print("\nAdding Student Record")

        id_no = input("Please input student ID Number --->")

        first_name = input("Please input student Fisrt Name --->").upper()
        second_name = input("PLease input student Second Name --->").upper()
        age = eval(input("Input student Age --->"))
        course = input("Input student Course --->").upper()
        section = input("Input student Section --->").upper()

        #STRONG DATA INTO A DICTIONARY - student_record
        student_record[id_no] = [first_name, second_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")
        #go back to original menu
        continue
    elif choice == 'b':
        os.system('cls')
        print("Printing Student Record")
        #Print(student_record) simple approach

        for i, j in student_record.items(): #Key - Values
            print(f"Student ID - {i}, Information {j}")
            continue

    elif choice == 'c':
        os.system('cls')
        print("Search Student Record")

        search_id = input("Input Student  ID for search --->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f"\nRecord Found for ID {search_id}")
                #to print the record for the search ID
                for i in student_record[search_id]:
                    print(f" ---{i}")
                print("==============================")
            else:
                print("No Record Found")
            break
        continue
    elif choice == 'd':
        os.system('cls')

        print("Delete Student Record")

        search_id = input("Input Student  ID for search --->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f"\nRecord Found for ID {search_id}")
                #to print the record for the search ID
                for i in student_record[search_id]:
                    print(f" ---{i}")
                print("==============================")
                #.pop() to delete an item
                student_record.pop(search_id)
                print("\nRecord Deleted")
            else:
                print("No Record Found")
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print("Edit/Modify Student Record")

        search_id = input("Input Student  ID for search --->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f"\nRecord Found for ID {search_id}")
                #to print the record for the search ID
                for i in student_record[search_id]:
                    print(f" ---{i}")
                print("==============================")
                #new sets set value for the searched ID
                first_name = input("Please input student Fisrt Name --->").upper()
                second_name = input("PLease input student Second Name --->").upper()
                age = eval(input("Input student Age --->"))
                course = input("Input student Course --->").upper()
                section = input("Input student Section --->").upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section

                print("Data Updated")
