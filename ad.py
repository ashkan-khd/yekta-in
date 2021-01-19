from __future__ import annotations

from typing import List, Dict

from base_model import BaseAdvertising


class Ad(BaseAdvertising):

    @classmethod
    def get_objects(cls):
        return cls.__ads

    def to_str(self):
        return self.get_title()

    __ads: List[Ad] = []

    def __init__(self, title: str, imgUrl: str, link: str, advertiser: object = None):
        super().__init__()
        self.__class__.__ads.append(self)
        self.__title: str = title
        self.__imgUrl: str = imgUrl
        self.__link: str = link
        self.__advertiser: object = advertiser

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_image_url(self) -> str:
        return self.__imgUrl

    def set_img_url(self, link: str) -> None:
        self.__imgUrl = link

    def get_link(self) -> str:
        return self.__link

    def set_link(self, link: str) -> None:
        self.__link = link

    def set_advertiser(self, advertiser: object) -> None:
        self.__advertiser = advertiser

    def describe_me(self) -> str:
        return 'this class store ad info'

    def inc_views(self) -> None:
        super().inc_views()
        self.__advertiser._views += 1

    def inc_clicks(self) -> None:
        super().inc_clicks()
        self.__advertiser._clicks += 1

    @staticmethod
    def get_object_data_in_json() -> List[Dict[str, int]]:
        __data: list = []
        for ad in Ad.__ads:
            __data.append({"ad id":ad.id, "ad title":ad.__title, "ad imgUrl": ad.__imgUrl, "ad link":ad.__link, "ad advertiser":None, "ad views":ad._views, "ad click": ad._clicks, "creation date": ad._creation_date.strftime("%Y/%m/%d %H:%M")})

        return __data
