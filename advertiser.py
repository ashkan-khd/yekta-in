from __future__ import annotations

from typing import List
from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    advertisers: List[Advertiser] = []

    def __init__(self, name) -> None:
        super().__init__()
        self.__class__.advertisers.append(self)
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name: str = name

    def describe_me(self) -> str:
        return 'this class store ad info'

    @classmethod
    def help(cls) -> str:
        return 'Id: id of this field is autoInc\nviews: nubmer of show of this ad\
            \nnumber: nubmer of click of this ad\nname: name of this ad'

    @staticmethod
    def get_total_clicks() -> int:
        clickSum: int = 0
        for adver in Advertiser.advertisers:
            clickSum += adver.clicks
        return clickSum

    @staticmethod
    def sort_by_date() -> List[Advertiser]:
        #TODO
        pass

    @staticmethod
    def get_object_data_in_json() -> List[Advertiser]:
        data: List[Advertiser] = []
        for adver in Advertiser.advertisers:
            data.append({"adver id":adver.id,"adver name":adver.name,"adver total clicks": adver.clicks, "adver total views": adver.views})

        return data

    @staticmethod
    def get_object_with_id(id) -> Advertiser:
        for advertiser in Advertiser.advertisers:
            if advertiser.id == id:
                return advertiser

        return None

    @classmethod
    def sort_and_get_objects(cls, sort_order: str = 'asc', sort_key: str = 'views'):
        return cls._sort_and_get_objects(cls.advertisers, sort_order, sort_key)
