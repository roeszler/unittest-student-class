""" Importing methods from the relevant modules """
from datetime import date, timedelta


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

        @property  # method to get data only
        def full_name(self):
            return f"{self._first_name} {self._last_name}"



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
