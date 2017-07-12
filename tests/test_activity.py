import unittest
from app.models.activity import Activity


class TestActivity(unittest.TestCase):
    """Test cases for the Activity class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.activity_1 = Activity('Swim with dolphins', 25)
        self.activity_2 = Activity('Visit Christ the redeemer', 23)

    def test_activity_instance(self):
        """This method tests if the Activity class creates an instance of itself"""
        self.assertIsInstance(self.activity_1, Activity,
                              msg='The object should be an instance of the `Activity` class')

    def test_instance_type(self):
        """This method tests if the Activity class creates a type of itself"""
        self.assertTrue((type(self.activity_2) is Activity), msg='The object should be of type `Activity`')

    def test_activity_attributes(self):
        """This method tests if the class assigns the right attributes to User instances"""
        self.assertEqual('Swim with dolphins', self.activity_1.name,
                         msg='The object first_name should be `Swim with dolphins`')

    def test_status_change(self):
        """This method tests if the Activity class changes the status of an instance"""
        self.activity_1.change_status(True)
        self.assertTrue(self.activity_1.status, msg='The object should be of have a status `True`')

    def test_rename(self):
        """This method tests if the Activity class changes the name of an instance"""
        self.activity_1.rename("Have fun!")
        self.assertEqual(self.activity_1.name, "Have fun!", msg='The object name should be `Have fun!`')

    def test_age_change(self):
        """This method tests if the Activity class changes the target_age of an instance"""
        self.activity_2.change_target_age(30)
        self.assertEqual(self.activity_2.target_age, 30, msg='The object target_age should be 30')

    def test_image_change(self):
        """This method tests if the Activity class changes the image url of an instance"""
        self.activity_1.change_image_url("app/static/img/gallery/activity_1.jpg")
        self.assertEqual(self.activity_1.image_url, "app/static/img/gallery/activity_1.jpg",
                         msg='The object image_url should be `app/static/img/gallery/activity_1.jpg`')


if __name__ == "__main__":
    unittest.main()
