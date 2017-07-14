import unittest
from datetime import datetime
from app.models.user import User
from app.models.bucketlist import BucketList
from app.models.sharing_pool import SharingPool
from app.models.activity import Activity


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.date_of_birth = datetime.strptime('Jun 1 1970', '%b %d %Y')
        self.activity_1 = Activity('Swim with dolphins', 25)
        self.bucketlist_1 = BucketList('Trip to Rio')
        self.bucketlist_2 = BucketList('Trip to Brazil')
        self.sharing_pool = SharingPool()

        self.bucketlists = {self.bucketlist_1.title: self.bucketlist_1}
        self.user_no_bucket = User('homie', 'duff', 'Homer', 'Simpson', self.date_of_birth)
        self.user_bucket = User('marge', 'maggie', 'Marge', 'Simpson', self.date_of_birth, self.bucketlists)

    def test_user_instance(self):
        """This method tests if the User class creates an instance of itself"""
        self.assertIsInstance(self.user_no_bucket, User,
                              msg='The object should be an instance of the `User` class')

    def test_type(self):
        """This method tests if the class creates a type of itself"""
        self.assertTrue((type(self.user_bucket) is User), msg='The object should be of type `User`')

    def test_user_attributes(self):
        """This method tests if the class assigns the right attributes to User instances"""
        self.assertEqual('Homer', self.user_no_bucket.first_name,
                         msg='The object first_name should be `Homer`')

    def test_change_password(self):
        """This method tests if the User class changes the password of an instance"""
        self.user_no_bucket.change_password("12345")
        self.assertEqual(self.user_no_bucket.password, "12345", msg='The object password should be `12345`')

    def test_change_birthday(self):
        """This method tests if the User class changes the birthday of an instance"""
        new_date_of_birth = datetime.strptime('Jul 1 1970', '%b %d %Y')
        self.user_no_bucket.change_birthday(new_date_of_birth)
        self.assertEqual(self.user_no_bucket.birthday, new_date_of_birth,
                         msg='The object birthday should be `Jul 1 1970`')

    def test_create_bucketlist(self):
        """This method tests if the class adds a bucketlist to User instances"""
        before = len(self.user_no_bucket.bucketlists)
        self.user_no_bucket.create_bucketlist(self.bucketlist_2)
        after = len(self.user_no_bucket.bucketlists)
        self.assertEqual(1, after - before,
                         msg='The object should add a bucket list to the instance')

    def test_remove_bucketlist(self):
        """This method tests if the class removes a bucketlist from User instances"""
        before = len(self.user_no_bucket.bucketlists)
        self.user_no_bucket.remove_bucketlist(self.bucketlist_2)
        after = len(self.user_no_bucket.bucketlists)
        self.assertEqual(1, before - after,
                         msg='The object should remove a bucket list from the instance')

    def test_share_bucketlist(self):
        """This method tests if the class shares a bucketlist from User instances"""
        before = len(self.sharing_pool.bucketlists)
        self.user_bucket.share_bucketlist(self.bucketlist_1)
        after = len(self.sharing_pool.bucketlists)
        self.assertEqual(1, after - before,
                         msg='The object should add a bucket list to the sharing pool')

    def test_share_activity(self):
        """This method tests if the class shares an activity from User instances"""
        before = len(self.sharing_pool.activities)
        self.user_bucket.share_activity(self.activity_1)
        after = len(self.sharing_pool.activities)
        self.assertEqual(1, after - before,
                         msg='The object should add an activity to the sharing pool')


if __name__ == "__main__":
    unittest.main()
