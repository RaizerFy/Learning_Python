##################### Hard Starting Project ######################
import random
import datetime as dt
import smtplib
import pandas as pd

## Put your real app password and email here and should work fine

my_email = "email@email.com"
password = "password"

list_of_msgs = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

my_file = pd.read_csv("birthdays.csv")
data = my_file.to_dict(orient="index")

birthday_dict = {}

## Loop for make every data on the CSV file padronized.
for key in data:
    birthday_dict.update({(data[key]["day"], data[key]["month"]): (data[key]["name"], data[key]["email"])})

now = dt.date.today()
data_time = now.timetuple()
day = data_time.tm_mday
month = data_time.tm_mon
today = (day, month)


if today in birthday_dict:
    name = birthday_dict.get(today)[0]
    email = birthday_dict.get(today)[1]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        random_msg = random.choice(list_of_msgs)
        with open(random_msg, "r") as txt:
            data_msg = txt.read()
            msg = data_msg.replace("[NAME]", name)

            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday \n\n {msg}"
                                )
            print("send it")






# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



