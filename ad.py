from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    ads = []
    def __init__(self, title, imgUrl, link, advertiser = None):
        super().__init__()
        self.__class__.ads.append(self)
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
        return 'this class store ad info'

    def incViews(self):
        super().incViews()
        self.advertiser.views +=1
        
    def incClicks(self):
        super().incClicks()
        self.advertiser.clicks +=1

    @staticmethod
    def object_data_in_json():
        data =[]
        for ad in Ad.ads:
            data.append({"ad id":ad.id, "ad title":ad.title, "ad imgUrl": ad.imgUrl, "ad link":ad.link, "ad advertiser":None, "ad views":ad.views, "ad click": ad.clicks, "creation date": ad.creation_date.strftime("%Y/%m/%d %H:%M") })

        return data
        
