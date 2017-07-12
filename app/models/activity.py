class Activity(object):
    """This class describes the structure of the Activity object"""

    def __init__(self, name, target_age, image_url="", status=False):
        """This method creates an instance of the Activity class"""
        self.name = name
        self.target_age = target_age
        self.image_url = image_url
        self.status = status

    def change_status(self, status):
        """This method changes the status in the Activity instance"""
        self.status = status
        return self.status

    def rename(self, name):
        """This method renames the Activity instance"""
        self.name = name
        return self.name

    def change_target_age(self, target_age):
        """This method changes the target age of the Activity instance"""
        self.target_age = target_age
        return self.target_age

    def change_image_url(self, image_url):
        """This method changes the image url of the Activity instance"""
        self.image_url = image_url
        return self.image_url

