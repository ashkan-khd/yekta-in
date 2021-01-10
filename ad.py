from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, title, imgUrl, link, advertiser):
        super().__init__()
        self.title = title
        self.imgUrl = imgUrl
        self.link = link
        self.advertiser = advertiser

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
        self.advertiser = advertiser

    def describeMe(self):
        super().describeMe()
        return 'this class store ad info'

    def incViews(self):
        super().incViews()
        self.advertiser.views +=1
        

    def incClicks(self):
        super().incClicks()
        self.advertiser.clicks +=1
        
