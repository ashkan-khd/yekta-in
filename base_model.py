class BaseAdvertising:
    id = -1
    clicks = 0
    views = 0

    def __init__(self):
        self.__class__.id += 1
        self.id = self.__class__.id
        self.views = 0
        self.clicks = 0
    def describeMe(self):
        'this is parent class'

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1
        __class__.clicks +=1

    def incViews(self):
        self.views += 1
        __class__.views += 1


