
import pandas
from datetime import *
import smtplib
today = datetime.now()
my_email = "sameerbashashaik2408@gmail.com"
my_password = "nfcbomhyhaeydztf"
today_tuple = (today.month, today.day)
data = pandas.read_csv("D:/birthday.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_file.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr="sameerbashashaik2408@gmail.com", to_addrs=birthday_person["e-mail"],
                            msg=f"subject:HAPPY_BIRTHDAY\n\n{contents}"
                            )

        connection.close()
