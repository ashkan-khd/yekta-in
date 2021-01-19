from __future__ import annotations

from abc import ABC, abstractmethod
import datetime


from typing import List


class BaseAdvertising(ABC):
    __next_id: int = -1

    def __init__(self):
        self.__class__.__next_id += 1
        self.id: int = self.__class__.__next_id
        self._views: int = 0
        self._clicks: int = 0
        self._creation_date: datetime = datetime.datetime.now()
        self.__class__.get_objects()[self.id] = self

    @abstractmethod
    def describe_me(self) -> str:
        raise NotImplementedError()

    @property
    def clicks(self) -> int:
        return self._clicks

    @property
    def views(self) -> int:
        return self._views

    def inc_clicks(self) -> None:
        self._clicks += 1

    def inc_views(self) -> None:
        self._views += 1

    @classmethod
    def __sort_by_clicks(cls, objects, sort_order):
        if sort_order.lower() == 'asc':
            objects.sort(key=lambda objects: objects._clicks)
        elif sort_order.lower() == 'dec':
            objects.sort(key=lambda objects: objects._clicks, reverse=True)
        else:
            raise Exception("Invalid Sort Order")

    @classmethod
    def __sort_by_views(cls, objects, sort_order):
        if sort_order.lower() == 'asc':
            objects.sort(key=lambda objects: objects._views)
        elif sort_order.lower() == 'dec':
            objects.sort(key=lambda objects: objects._views, reverse=True)
        else:
            raise Exception("Invalid Sort Order")

    @classmethod
    def sort_and_get_objects(cls, sort_order: str = 'asc', sort_key: str = 'views') -> List[BaseAdvertising]:
        objects = list(cls.get_objects().values())
        if sort_key == 'clicks':
            cls.__sort_by_clicks(objects, sort_order)
        elif sort_key == 'views':
            cls.__sort_by_views(objects, sort_order)
        else:
            raise Exception("Invalid Sort Key")
        return objects

    def __str__(self):
        return self.to_str() + ', clicks:' + str(self.clicks) + ', views: ' + str(self.views)

    @abstractmethod
    def to_str(self):
        pass

    @classmethod
    @abstractmethod
    def get_objects(cls):
        pass

    @classmethod
    def get_object_with_id(cls, id):
        return cls.get_objects().get(id, None)

    # O(1) < O(logn) < O(n) < O(n^2) < O(a^n) < O(n!)