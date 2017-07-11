import unittest
from app.models.activity import Activity
from app.models.bucketlist import BucketList


class TestBucketList(unittest.TestCase):
    """Test cases for the BucketList class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.activity_1 = Activity('Swim with dolphins', 25)
        self.activity_2 = Activity('Visit Christ the redeemer', 23)
        self.activity_3 = Activity('Naked walk on the beach', 20)

        self.activities = {self.activity_1.name: self.activity_1, self.activity_2.name: self.activity_2}
        self.bucketlist_1 = BucketList('Trip to Rio')
        self.bucketlist_2 = BucketList('Trip to Brazil', self.activities)

    def test_bucketlist_instance(self):
        """This method tests if the BucketList class creates an instance of itself"""
        self.assertIsInstance(self.bucketlist_1, BucketList,
                              msg='The object should be an instance of the `BucketList` class')

    def test_instance_type(self):
        """This method tests if the BucketList class creates a type of itself"""
        self.assertTrue((type(self.bucketlist_2) is BucketList), msg='The object should be of type `BucketList`')

    def test_bucketlist_attributes(self):
        """This method tests if the class assigns the right attributes to BucketList instances"""
        self.assertEqual('Trip to Rio', self.bucketlist_1.title,
                         msg='The object first_name should be `Trip to Rio`')

    def test_add_activity(self):
        """This method tests if the class adds an activity to BucketList instances"""
        before = len(self.bucketlist_1.activities)
        self.bucketlist_1.add_activity(self.activity_3)
        after = len(self.bucketlist_1.activities)
        self.assertEqual(1, after - before,
                         msg='The object should add an activity to the instance')

    def test_remove_activity(self):
        """This method tests if the class removes an activity from BucketList instances"""
        before = len(self.bucketlist_1.activities)
        self.bucketlist_1.remove_activity(self.activity_3)
        after = len(self.bucketlist_1.activities)
        self.assertEqual(1, before - after,
                         msg='The object should remove an activity from the instance')

    def test_change_title(self):
        """This method tests if the BucketList class changes the title of an instance"""
        self.bucketlist_1.change_title("My bucket")
        self.assertEqual(self.bucketlist_1.title, "My bucket", msg='The object title should be `My bucket`')


if __name__ == "__main__":
    unittest.main()
