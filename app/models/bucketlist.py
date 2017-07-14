class BucketList(object):
    """This class describes the structure of the BucketList object"""

    def __init__(self, title, activities={}):
        """This method creates an instance of the BucketList class"""
        self.title = title
        self.activities = activities

    def add_activity(self, activity):
        """This method creates an activity in the BucketList instance"""
        self.activities[activity.name] = activity
        return self.activities
       
    def remove_activity(self, activity):
        """This method removes an activity from the BucketList instance"""
        if activity.name in self.activities.keys():
            del self.activities[activity.name]
        return self.activities

    def change_title(self, title):
        """This method changes the title of the BucketList instance"""
        self.title = title
        return self.title

