import smtplib
#  Email SMPT Documentation  #  https://docs.python.org/3/library/smtplib.html
from datetime import datetime as dt
#  Date Time Documentation  #  https://docs.python.org/3/library/datetime.html
import pandas as pd
from random import randint

my_email = "andrewjash.py@outlook.com"
my_email_connection = "outlook.office365.com"

second_email = "andrewjash.py@yahoo.com"
second_email_connection = "smtp.mail.yahoo.com"

e_pass = ""


##################### Extra Hard Starting Project ######################

#TODO 1. Update the birthdays.csv
#Updated Andrew,andrewjash.py@yahoo.com,1986,6,23 in birthdays.csv file

#TODO 2. Check if today matches a birthday in the birthdays.csv, only day and month matter
now = dt.now()
check_month = now.month
check_day = now.day

with open("birthdays.csv") as data_file:
    data = pd.read_csv("birthdays.csv")
    data = data.to_dict(orient="records")
    # print(data)

    for _ in range(len(data)):
        bd_name = data[_]["name"]
        bd_month = data[_]["month"]
        bd_day = data[_]["day"]
        # print(bd_month)
        # print(bd_day)
    if check_month == bd_month and check_day == bd_day:
        # print(f"Today is {bd_name}'s Birthday")
        # TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter_file:
            contents = letter_file.read()
            # print(contents)
            new_contents = contents.replace("[NAME]", bd_name)
            print(new_contents)


        # # TODO 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(my_email_connection) as connection:
            connection.starttls()  # secure the email connection
            connection.login(user=my_email, password=e_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=second_email,
                                msg="Subject:Happy Birthday 2\n\n"
                                    f"{new_contents}")

            print("Msg Sent")
    else:
        print("No one has a birthday today")




# Angela Code
# today = dt.now()
# today_tuple = (today.month, today.day)
#
#
# with open("birthdays.csv") as data_file:
#     data = pd.read_csv("birthdays.csv")
#
#     # birthdays_dict = {
#     #     (birthday_month, birthday_day): data_row
#     # }
#     # Dictionary comprehension template for pandas DataFrame looks like this:
#     # new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#     birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#
#     if today_tuple in birthday_dict:
#         birthday_name = birthday_dict[today_tuple]["name"]
#         file_path = f"letter_templates/letter_{randint(1,3)}.txt"
#         # print(file_path)
#         with open(file_path) as letter_file:
#             contents = letter_file.read()
#             new_contents = contents.replace("[NAME]", birthday_name)
#             print(new_contents)
#
#         with smtplib.SMTP(my_email_connection) as connection:
#             connection.starttls()  # secure the email connection
#             connection.login(user=my_email, password=e_pass)
#             connection.sendmail(from_addr=my_email,
#                                 to_addrs=second_email,
#                                 msg="Subject:Happy Birthday\n\n"
#                                     f"{new_contents}")
#
#             print("Msg Sent")
