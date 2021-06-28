import smtplib
#  Email SMPT Documentation  #  https://docs.python.org/3/library/smtplib.html
import datetime as dt
#  Date Time Documentation  #  https://docs.python.org/3/library/datetime.html
from random import choice

my_email = "andrewjash.py@outlook.com"
my_email_connection = "outlook.office365.com"

second_email = "andrewjash.py@yahoo.com"
second_email_connection = "smtp.mail.yahoo.com"

e_pass = "GeK7Z!SP5!*cE"


# my_email = "andrewjash.py@outlook.com"
# my_email_connection = "outlook.office365.com"
#
# second_email = "andrewjash.py@yahoo.com"
# second_email_connection = "smtp.mail.yahoo.com"
# yahoo_pass = "cvfdefewhyfxcrzy"
#
# third_email = "andrewjash.py@gmail.com"
# third_email_connection = "smtp.gmail.com"
#
# e_pass = "GeK7Z!SP5!*cE"
#
# with smtplib.SMTP(second_email_connection) as connection:
#     connection.starttls() # secure the email connection
#     connection.login(user=second_email, password=yahoo_pass)
#     connection.sendmail(from_addr=second_email,
#                         to_addrs=my_email,
#                         msg="Subject:Hello\n\n"
#                             "This is the body of my email")
#
#     print("Msg Sent")



# ---------- Date / Time Methods ---------- #
# now = dt.datetime.now() # Gets current date and time
# # year = now.year
# # month = now.month
# # day = now.day
# # day_of_week = now.weekday() # returns a number, 0-6
# # hour = now.hour
# # minute = now.minute
# date_of_birth = dt.datetime(year=1986, month=12, day=29)
# print(date_of_birth )


#TODO-1: Use datetime to obtain current day of the week
now = dt.datetime.now()
dow = now.isoweekday() # Monday is 1 and Sunday is 7
# print(dow)

#TODO-2: Open the quotes.txt file and obtain a list of quotes
with open("data/quotes.txt") as data_file:
    data = data_file.readlines() # Saves data as string type
    # TODO-3: Use random module to pick a random quote
    random_quote = choice(data)
    # print(random_quote)

# TODO-4: Use smtplib to email yourself on wednesdays
if dow == 3:
    with smtplib.SMTP(my_email_connection) as connection:
        connection.starttls() # secure the email connection
        connection.login(user=my_email, password=e_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs=second_email,
                            msg="Subject:Random Wednesday Motivation\n\n"
                                f"{random_quote}")

        print("Msg Sent")
else:
    print("It's not Monday")