import csv
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# Function to read the CSV file and extract birthday data
def read_csv():
    birthdays = []
    with open("birthdays.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            birthdays.append(row)
    return birthdays

# Function to select a random letter
def select_random_letter():
    letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
    letter_file = random.choice(letters)
    with open(letter_file, 'r') as file:
        letter_content = file.read()
    return letter_content

# Function to check if today is someone's birthday
def check_birthday(birthdays):
    today = dt.datetime.now().strftime('%m-%d')
    for person in birthdays:
        birthday = "{}-{}".format(person['month'], person['day'])
        if today == birthday:
            print("Today is {}'s birthday! 🎉".format(person['name']))
            print("Born on: {}".format(today))
            return person
    return None


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "smwangilewis@gmail.com"
password = "aebi wdxy jmsr xzza"

# Check if today is someone's birthday
birthday_person = check_birthday(read_csv())
if birthday_person:
    print("Happy Birthday, {}!".format(birthday_person['name']))
    # Get the recipient's email address
    recipient_email = birthday_person['email']
    # Get a random letter template
    letter_template = select_random_letter()
    # Replace [NAME] with the person's actual name from birthdays.csv
    letter_content = letter_template.replace("[NAME]", birthday_person['name'])
    print(letter_content)
    # sending email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject:HAPPY BIRTHDAY\n{letter_content}")
        connection.close()
else:
    print("No birthdays today. 😔")

# sending email
# def send_email(letter_content, recipient_email):
#     # Set up the SMTP server
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=select_random_letter())
#         connection.close()
