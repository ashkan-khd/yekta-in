from typing import List

from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    ads: list = []
    def __init__(self, title: str, imgUrl: str, link: str, advertiser: object = None):
        super().__init__()
        self.__class__.ads.append(self)
        self.title: str = title
        self.imgUrl: str = imgUrl
        self.link: str = link
        self.advertiser: object = advertiser

    def getTitle(self) -> str:
        return self.title

    def setTitle(self, title) -> None:
        self.title = title

    def getImageUrl(self) -> str:
        return self.imgUrl

    def setImgUrl(self, link) -> None:
        self.imgUrl = link

    def getLink(self) -> str:
        return self.link

    def setLink(self, link) -> None:
        self.link = link

    def setAdvertiser(self, advertiser) -> None:
        self.advertiser = advertiser

    def describeMe(self) -> str:
        return 'this class store ad info'

    def incViews(self) -> None:
        super().incViews()
        self.advertiser.views +=1

    def incClicks(self) -> None:
        super().incClicks()
        self.advertiser.clicks +=1

    @staticmethod
    def getObjectDataInJson() -> List[dict]:
        data =[]
        for ad in Ad.ads:
            data.append({"ad id":ad.id, "ad title":ad.title, "ad imgUrl": ad.imgUrl, "ad link":ad.link, "ad advertiser":None, "ad views":ad.views, "ad click": ad.clicks, "creation date": ad.creation_date.strftime("%Y/%m/%d %H:%M") })

        return data

    @staticmethod
    def getObjectWithId(id) -> object:
        for ad in Ad.ads:
            if ad.id == id:
                return ad

        return None

    @classmethod
    def sort_and_get_object_by_key(cls, sortOrder: str = 'asc', sortKey: str = None, objects: object =None) -> List[object]:
        return super(Ad, cls).sort_and_get_object_by_key(sortOrder=sortOrder, sortKey=sortKey, objects=cls.ads)




