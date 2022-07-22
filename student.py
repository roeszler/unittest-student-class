"""
Importing methods from the relevant modules
"""
# import datetime
from datetime import date, timedelta
import requests


class Student:
    """
    A student class as a base for method testing.
    When an instance of our Student class is created,
    the start_date value is set using the time at
    the moment of the instance's creation.
    """
    def __init__(self, first_name, last_name):
        """
        " _ " at beginning indicates to be a read only field in the db
        """
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.attention_list = False

    @property  # read only method to get data only
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    

    def alert_behaviour(self):
        """ to modify the attention_list property (not return a value) """
        self.attention_list = True


    @property # read only method
    def email(self):
        """
        read only method to return email 
        """
        # return lower(f"{self._first_name}.{self._last_name}@email.com")
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    
    def apply_extension(self, days_to_increment):
        """
        Updates the end_date by adding days to it.
        Syntax : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) Returns : Date
        timedelta() used for calculating differences in dates
        """
        self.end_date = self.end_date + timedelta(days=days_to_increment)


    def course_schedule(self):
        """
        Makes a request to our fictional API service
        We get a student's course schedule using requests.get
        Store it in a variable called response,  and 
        Return either the response text or an error message.
        """
        response = requests.get(
            f"https://company.com/course-schedule/{self._last_name}/{self._first_name}"
            )
        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request to the server!"


# ------------ Test code

# ------------ Leap year days

# input_year = int(datetime.datetime.now().strftime("%G"))
# if ((input_year % 400 == 0) or (
#     (input_year % 4 == 0) and (input_year % 100 != 0)
#     )):
#     print("%d is Leap Year" % input_year)
#     days = 366
# else:
#     print("%d is Not the Leap Year" % input_year)
#     days = 365
