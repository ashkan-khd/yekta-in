from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, title, imgUrl, link, advertise ):
        super().__init__()
        self.title = title
        self.imgUrl = imgUrl
        self.link = link

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getImageUrl(self):
        return self.imgUrl

    def setImgUrl(self, link):
        self.imgUrl = link

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link

    def setAdvertiser(self, advertiser):
        self.advertiser = advertiser.name

    def describeMe(self):
        super().describeMe()
        return 'this class store ad info'




