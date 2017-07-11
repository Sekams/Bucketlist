class SharingPool(object):
    """This class holds the items to be shared"""

    def __init__(self, bucketlists={}, activities={}):
        """This method creates an instance of the SharingPool"""
        self.bucketlists = bucketlists
        self.activities = activities

    def add_bucket(self, username, bucketlist):
        """This method adds a buckectlist to the SharingPool"""
        sharing_pool_bucketlists = []
        if username in self.bucketlists.keys():
            sharing_pool_bucketlists = self.bucketlists[username]
        sharing_pool_bucketlists.append(bucketlist)
        self.bucketlists[username] = sharing_pool_bucketlists

    def add_activity(self, username, activity):
        """This method adds an activity to the SharingPool"""
        sharing_pool_activities = []
        if username in self.activities.keys():
            sharing_pool_activities = self.activities[username]
        sharing_pool_activities.append(activity)
        self.activities[username] = sharing_pool_activities

