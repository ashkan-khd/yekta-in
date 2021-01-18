from __future__ import annotations

from abc import ABC, abstractmethod
import datetime


from typing import List


class BaseAdvertising(ABC):
    __id: int = -1

    def __init__(self):
        self.__class__.__id += 1
        self.id: int = self.__class__.__id
        self._views: int = 0
        self._clicks: int = 0
        self._creation_date: datetime = datetime.datetime.now()

    @abstractmethod
    def describe_me(self) -> str:
        raise NotImplementedError()

    def get_clicks(self) -> int:
        return self._clicks

    def get_views(self) -> int:
        return self._views

    def inc_clicks(self) -> None:
        self._clicks += 1

    def inc_views(self) -> None:
        self._views += 1

    @classmethod
    def _sort_and_get_objects(cls, objects: List[BaseAdvertising], sort_order: str = 'asc', sort_key: str = 'views') -> List[BaseAdvertising]:
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

    @abstractmethod
    @classmethod
    def sort_and_get_objects(cls, sortOrder: str = 'asc', sortKey: str = 'views'):
        pass
