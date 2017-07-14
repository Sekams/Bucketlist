from app.models.sharing_pool import SharingPool

class User(object):
    """This class describes the structure of the User object"""

    def __init__(self, username, password, first_name, last_name, birthday, bucketlists={}):
        """This method creates an instance of the User class"""
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.bucketlists = bucketlists
        self.sharing_pool = SharingPool()

    def change_password(self, password):
        """This method changes the password of the User instance"""
        self.password = password
        return self.password
       
    def change_birthday(self, birthday):
        """This method changes the birthday of the User instance"""
        self.birthday = birthday
        return self.birthday

    def create_bucketlist(self, bucketlist):
        """This method creates a bucketlist in the User instance"""
        self.bucketlists[bucketlist.title] = bucketlist
        return self.bucketlists

    def remove_bucketlist(self, bucketlist):
        """This method removes a bucketlist from the User instance"""
        if bucketlist.title in self.bucketlists.keys():
            del self.bucketlists[bucketlist.title]
        return self.bucketlists

    def share_bucketlist(self, bucketlist):
        """This method shares a bucketlist from the User instance"""
        if bucketlist.title in self.bucketlists.keys():
            self.sharing_pool.add_bucket(self.username, bucketlist)
        return self.sharing_pool.bucketlists

    def share_activity(self, activity):
        """This method shares an activity from the User instance"""
        self.sharing_pool.add_activity(self.username, activity)
        return self.sharing_pool.activities


