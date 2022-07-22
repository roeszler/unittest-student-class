import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod #  acts on the  class instead of an instance of the class.
    def setUpClass(cls):
        print("setUpClass")


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    def setUp(self):
        """
        self.student creates it as an instance variable and thus all
        refrences of student now need to be changed to self.student
        the setUp method can be used to  create temporary files and folders
        or set up  a database connection during tests
        """
        print("setup") # Just so we can see when the setUp method is run
        # self.student creates it as an instance variable so we can remove its 
        # repetition from the lines of code:
        self.student = Student("John", "Doe")
    

    def tearDown(self):
        """
        used to remove temporary files or folders or close a connection to a database.
        """
        print("tearDown")
    

    def test_full_name(self):
        # student = Student("John", "Doe")
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")
    

    def test_alert_behaviour(self):
        # student = Student("John", "Doe")
        print("test_alert_behaviour")
        self.student.alert_behaviour()
        self.assertTrue(self.student.attention_list)
    

    def test_email(self):
        # student = Student("John", "Doe")
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


if __name__ == '__main__':
    """
    Not required, however placed in anyway:
    Will run the file without having to specify the Unittest module.
    Will only run unittest.main() if it is run as the 'main' file. 
    Will not run if test_student.py is run as an 'import'. 
    """
    unittest.main()