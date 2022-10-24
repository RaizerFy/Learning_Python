# import smtplib
#
# my_email = "sideprojectpython@gmail.com"
# password = "pczjsspppmrjgjok"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="marcao.kbs@gmail.com",
#                         msg="Subject:Hello\n\n This is the body")

# import datetime as dt
#
# now = dt.datetime.now()
#
# date_of_birth = dt.datetime(year=1997, month=4, day=22)
#
#
# print(date_of_birth)
# print(now)

import datetime as dt
import smtplib
import random


my_email = "email@email.com"
password = "password"
now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

with open("quotes.txt", "r") as file:
    quotes = file.read()
    list_of_quotes = quotes.splitlines()


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if day_of_week ==  5:
        msg = random.choice(list_of_quotes)
        print(msg)
        connection.sendmail(from_addr=my_email,
                            to_addrs="marcao.kbs@gmail.com",
                            msg=f"{msg}")
        print("Send it")
    else:
        print("Something goes wrong")




