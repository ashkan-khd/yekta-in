from __future__ import annotations

from typing import List, Dict
from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):

    @classmethod
    def get_objects(cls):
        return cls.__advertisers

    def to_str(self):
        return self.get_name()

    __advertisers: Dict[int, Advertiser] = {}

    def __init__(self, name) -> None:
        super().__init__()
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
        for adver in Advertiser.__advertisers:
            clickSum += adver.clicks
        return clickSum

    @staticmethod
    def sort_by_date() -> List[Advertiser]:
        #TODO
        pass

    @staticmethod
    def get_object_data_in_json() -> List[Advertiser]:
        data: List[Advertiser] = []
        for adver in Advertiser.__advertisers:
            data.append({"adver id":adver.id,"adver name":adver.name,"adver total clicks": adver.clicks, "adver total views": adver.views})

        return data
