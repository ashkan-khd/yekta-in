from abc import ABC, abstractmethod
import datetime


from typing import List


class BaseAdvertising(ABC):
    id: int = -1

    def __init__(self):
        self.__class__.id += 1
        self.id: int = self.__class__.id
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
    def sort_and_get_object_by_key(cls, sortOrder: str = 'asc', sortKey: str = 'views', objects: object = None) -> List[object]:
        if sortKey == 'clicks':
            if sortOrder.lower() == 'asc':
                objects.sort(key=lambda objects: objects._clicks)
            elif sortOrder.lower() == 'dec':
                objects.sort(key=lambda objects: objects._clicks, reverse=True)
            else:
                raise Exception("invalid sortkey")
        elif sortKey == 'views':
            if sortOrder.lower() == 'asc':
                objects.sort(key=lambda objects: objects._views)
            elif sortOrder.lower() == 'dec':
                objects.sort(key=lambda objects: objects._views, reverse=True)
            else:
                raise Exception("invalid sortkey")

        return objects
