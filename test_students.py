import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
    

    def test_alert_behaviour(self):
        student = Student("John", "Doe")
        student.alert_behaviour()

        self.assertTrue(student.attention_list)


if __name__ == '__main__':
    """
    Not required, however placed in anyway:
    Will run the file without having to specify the Unittest module.
    Will only run unittest.main() if it is run as the 'main' file. 
    Will not run if test_student.py is run as an 'import'. 
    """
    unittest.main()