
# Employee Username, Password, Email address and other info generator program.
# Neil Stratton - March 3, 2022
# Sprint week  - Fun wih Strings

import datetime
import random

LINE = (f"-" * 55)

# Display
def display():
    print("[Employee Info Program with Username and Password Generator]")
    print("")

# Inputs and validation:
while True:
    display()
    while True:
        emp_phone_number = str(input("Enter employee phone number 10 digits 999-999-9999 format: ")).upper()
        length = len(emp_phone_number)
        if length == 12 \
                and emp_phone_number[3] == "-" \
                and emp_phone_number[7] == "-" \
                and emp_phone_number[:3].isdigit() \
                and emp_phone_number[4:7].isdigit() \
                and emp_phone_number[8:].isdigit():
            print("")
        else:
            print("Invalid Phone Number")
            continue
        break

    while True:
        try:
            emp_first_name = str(input("Enter employee first name: "))
            if emp_first_name.isalpha():
                pass
            else:
                raise TypeError
        except TypeError:
            print("Invalid First Name")
        else:
            break

    while True:
        try:
            emp_last_name = str(input("Enter employee last name: "))
            if emp_last_name.isalpha():
                print("")
            else:
                raise TypeError
        except TypeError:
            print("Invalid Last Name")
        else:
            break

    while True:
        try:
            emp_start_date = str(input("Enter the employee start date : YYYY-MM-DD format: "))
            emp_start_date = datetime.datetime.strptime(emp_start_date, "%Y-%m-%d")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break

    while True:
        try:
            emp_birth_date = str(input("Enter the employee Birthday : YYYY-MM-DD format: "))
            emp_birth_date = datetime.datetime.strptime(emp_birth_date, "%Y-%m-%d")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break

# Convert date to string and remove dashes and unwanted characters, so they won't be in password
    date_string = emp_start_date.strftime('%Y%m%d')
    bday_string = emp_birth_date.strftime('%Y%m%d')
    emp_phone_number_pass = emp_phone_number.replace('-', "")
    emp_first_name_pass = emp_first_name.replace("O", "")
    emp_last_name_pass = emp_last_name.replace("O", "")

# Current date and time and convert to string
    cur_day = datetime.datetime.today()
    cur_time = datetime.datetime.now()
    cur_day_string = cur_day.strftime('%B, %d, %Y')
    cur_time_string = cur_time.strftime('%H:%M:%S')

# Convert employee Birthdate to string and calculation age
    bday_full = emp_birth_date.strftime("%B")
    year_difference = cur_day.year - emp_birth_date.year
    days_company = emp_birth_date.day - cur_day.day

# Username and password conversion variables
    symbols = ("%!#$@&*")
    alpha_chars = ("AaBbCcDdEeFfGgHhIiJjKkLlMmNnPpQqRrSsTtUuVvWwXxYyZz")

# Combine first name and last name to check length for password options
    length = str(emp_first_name + emp_last_name)
    if len(length) <= 5:
        password_list = (alpha_chars + emp_first_name_pass + emp_last_name_pass + date_string + bday_string + emp_phone_number_pass + symbols)
    else:
        password_list = (emp_first_name_pass + emp_last_name_pass + date_string + bday_string + emp_phone_number_pass + symbols)

# Randomize the password mix and output password length
    password_mix = random.choices(password_list, k=10)
    password_final = (password_mix[0] + password_mix[1] + password_mix[2] + password_mix[3] + password_mix[4] + \
                      password_mix[5] + password_mix[6] + password_mix[7] + password_mix[8] + password_mix[9])

# Create username
    user_name = (f"{emp_first_name[0].title()}.{emp_last_name[0].title()}{emp_last_name[1:]}")

# Adjust header lines depending on length of email address
    email_length = (f"Email Address is:     {emp_first_name.lower()}.{emp_last_name.lower()}@nlchocolatecompany.com")
    num = int(len(email_length))
    LINE = (f"-" * num)

# Output display
    print("")
    print(f"EMPLOYEE REPORT:")
    print(f"{LINE}")
    print("Current Day and Time:")
    print(f"{LINE}")
    print(f" Today's Date is :    {cur_day_string}")
    print(f" Current Time is:     {cur_time_string}")
    print("")
    print(f"{LINE}")
    print(f"Employee Username, Password and Email Address: ")
    print(f"{LINE}")
    print(f" Username is:         {user_name}")
    print(f" Password is:         {password_final}")
    print(f" Email Address is:    {emp_first_name.lower()}.{emp_last_name.lower()}@nlchocolatecompany.com")
    print("")
    print(f"{LINE}")
    print(f"Other Employee info:")
    print(f"{LINE}")
    print(f" First name:           {emp_first_name.title()}")
    print(f" Last Name:            {emp_last_name.title()}")
    print(f" Phone Number:         {emp_phone_number}")
    print("")
    print(f" {emp_first_name.title()}'s Birthday is in {bday_full} ")
    print(f" {emp_first_name.title()} is {year_difference} Years old")
    print("")
    print(f"{LINE}")

    enter_new_info = input("Would you like to enter a info Y for Yes: ").upper()
    print("")
    if enter_new_info == "Y":
        continue
    else:
        break






















