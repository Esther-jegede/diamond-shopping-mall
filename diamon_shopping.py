# algorithm to open an account with a shopping mall
import fileinput
from random import randint
import string
import http
import urllib
import requests
import sep as sep
from beautifulsoup4 import beautifulsoup4
import random
# import request allows you to send https requests
# username should be at least 4-20 characters
created = []
import gettext
import http.server


def save_account(username, password):
    username = username
    password = password
    sep = sep
    fid = open("Created account.txt," "w")
    fid.write("\n%s%s%%s\t" + "time ") % (username, sep, password)
    fid.close()
    created.append(username)

    def create_account(region, password, number, sep):
        region = region
        password = password
        sep = sep


# sep is to separate
# send url using the region entered by the user
def region(region):
    region = region


url = "https://signup." + region + " diamondshoppingmall.com/signup/index/"
# creating a random username

fid = open("names")
names = fid.readlines()
names2 = random.choice (names)
username = names2[:len(names2) - 1] + str(randint(100, 1000))


# creating an account with a random username + @gmail.com


email = username + "@gmail.com"


def password(password):
    password = password


# checking password validity And creating random password

if len(password) >= 8:
    if password == "":

        def identity_generator(size=8, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars))
    elif password != "":
        print("invalid password")

        dob = []
        dob.append(randint(1, 30))
        dob.append(randint(1, 12))
    dob.append(randint(1920, 2012))

dd = dob[0]
mm = [1]
yyyy = [2]

print("URL: ") % url
print("Region: ") % region
print("Email: ") % email
print("Date Of Birth: ") % (str(dob[0]), dob[1], dob[2])


def main():
    print("regions: EUNE, EUW, NA, LAN, LAS, BR")
    print(" Password may only contain letters and numbers")
    region = input(" Region :")
    password = input(" password")
