from typing import List, Dict

from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    ads: list = [object]

    def __init__(self, title: str, imgUrl: str, link: str, advertiser: object = None):
        super().__init__()
        self.__class__.ads.append(self)
        self.title: str = title
        self.imgUrl: str = imgUrl
        self.link: str = link
        self.advertiser: object = advertiser

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_image_url(self) -> str:
        return self.imgUrl

    def set_img_url(self, link: str) -> None:
        self.imgUrl = link

    def get_link(self) -> str:
        return self.link

    def set_link(self, link: str) -> None:
        self.link = link

    def set_advertiser(self, advertiser: object) -> None:
        self.advertiser = advertiser

    def describe_me(self) -> str:
        return 'this class store ad info'

    def inc_views(self) -> None:
        super().inc_views()
        self.advertiser.views += 1

    def inc_clicks(self) -> None:
        super().inc_clicks()
        self.advertiser.clicks += 1

    @staticmethod
    def get_object_data_in_json() -> List[Dict[str, int, object]]:
        data: list = [object]
        for ad in Ad.ads:
            data.append({"ad id":ad.id, "ad title":ad.title, "ad imgUrl": ad.imgUrl, "ad link":ad.link, "ad advertiser":None, "ad views":ad.views, "ad click": ad.clicks, "creation date": ad.creation_date.strftime("%Y/%m/%d %H:%M") })

        return data

    @staticmethod
    def get_object_with_id(id) -> object:
        for ad in Ad.ads:
            if ad.id == id:
                return ad

        return None

    @classmethod
    def sort_and_get_object_by_key(cls, sortOrder: str = 'asc', sortKey: str = None, objects: object =None) -> List[object]:
        return super(Ad, cls).sort_and_get_object_by_key(sortOrder=sortOrder, sortKey=sortKey, objects=cls.ads)




