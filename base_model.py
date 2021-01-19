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
    def sort_and_get_objects(cls, sort_order: str = 'asc', sort_key: str = 'views') -> List[BaseAdvertising]:
        objects = cls.get_objects()
        if sort_key == 'clicks':
            if sort_order.lower() == 'asc':
                objects.sort(key=lambda objects: objects._clicks)
            elif sort_order.lower() == 'dec':
                objects.sort(key=lambda objects: objects._clicks, reverse=True)
            else:
                raise Exception("invalid sortkey")
        elif sort_key == 'views':
            if sort_order.lower() == 'asc':
                objects.sort(key=lambda objects: objects._views)
            elif sort_order.lower() == 'dec':
                objects.sort(key=lambda objects: objects._views, reverse=True)
            else:
                raise Exception("invalid sortkey")

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
        for object in cls.get_objects():
            if object.id == id:
                return object

        return None