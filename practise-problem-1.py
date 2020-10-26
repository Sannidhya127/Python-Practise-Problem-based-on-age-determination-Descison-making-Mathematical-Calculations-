# Practice Problem 1 (Easy) | Python Tutorials For Absolute Beginners In Hindi #103
# The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your performance.

# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:

# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!


import time
from datetime import date


def ContinueOrExit():
    print("Press q to quit and c to continue")
    user_choice2 = ""
    while(user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue


def BirthYearExtractData():
    extra = input(
        "Do you want to know what your age will be in a particular year? if yes then type 'Yes' or else type 'No':\n")

    extra = extra.lower()
    if extra == "yes":
        year = int(
            input("Please enter the year you want your age to be counted from now:\n"))
        time.sleep(0.90)
        print("Please wait while we manipulate the data for you")
        time.sleep(1)
        if ageOrYear == brithYear:
            aged = year - brithYear
            print(f"You will be {aged} in the year {year}")
            time.sleep(3)
            print("Thank You for using our system")
            print("We are glad you used this")
        elif extra == "no":
            print(
                "We are delighted to provide you with our services. Looking forward to serve you again")
        time.sleep(6)

        return "Looking forward to serve you again"


def AgeGivenExtractData():
    extra = input(
        "Do you want to know what your age will be in a particular year? if yes then type 'Yes' or else type 'No':\n")

    extra = extra.lower()
    if extra == "yes":
        year = int(
            input("Please enter the year you want your age to be counted from now:\n"))
        time.sleep(0.90)
        print("Please wait while we manipulate the data for you")
        time.sleep(1)
        if year < current_date.year:
            print("We kindly request you not to joke with our system as we can understand very nicely that you have entered an year which has already past by")
        elif year > current_date.year:
            InitialResult = year - current_date.year
            ageNow = InitialResult + age
            print(f"Your age will be {ageNow} in the year {year}")
            print(
                'Thank You for using our system. We are glad to provide you our services')

            time.sleep(6)
    elif extra == "no":
        print("Thank you for using our system. We are glad to provide you our services")
        time.sleep(6)
    else:
        print("Your input is invalid. Please try again")
        time.sleep(6)

    return "Looking forward to serve you again"


if __name__ == "__main__":

    current_date = date.today()
    print(current_date)
    # print(current_date.year)

    ageOrYear = int(input("Please enter your age or the birth year:\n"))
    # print(type(ageOrYear))
    if ageOrYear > 150:
        brithYear = ageOrYear
        # print(f"The birth year is {brithYear}")
        if brithYear < current_date.year:
            HundredLater = brithYear + 100
            print(f"You will become 100 years old in th year {HundredLater}")
            print(BirthYearExtractData())
        elif brithYear > current_date.year:
            print("Sorry dear! My System is not that fool that it cannot understand that you aren't yet born. Go become born and then come back")
            print(BirthYearExtractData())

    else:
        age = ageOrYear
        # print(f"Age is {age}")
        if age >= 100:
            print("Dear old person, as you have already turned hundred its better you go home instead of wasting our time here")
            print(AgeGivenExtractData())

        else:
            timePeriod = 100 - age
            yearOfHundred = timePeriod+current_date.year
            print(
                f"You will turn 100 years old {timePeriod} years later in the year {yearOfHundred}")
            print(AgeGivenExtractData())

    # print(ContinueOrExit())
