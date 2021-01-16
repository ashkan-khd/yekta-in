from abc import ABC, abstractmethod
import datetime


from typing import List


class BaseAdvertising(ABC):
    id: int = -1

    def __init__(self):
        self.__class__.id += 1
        self.id: int = self.__class__.id
        self.views: int = 0
        self.clicks: int = 0
        self.creation_date: datetime = datetime.datetime.now()

    @abstractmethod
    def describeMe(self) -> str:
        raise NotImplementedError()

    def getClicks(self) -> int:
        return self.clicks

    def getViews(self) -> int:
        return self.views

    def incClicks(self) -> None:
        self.clicks += 1

    def incViews(self) -> None:
        self.views += 1

    @classmethod
    def sort_and_get_object_by_key(cls, sortOrder='asc', sortKey='views', objects=None) -> List[object]:
        if sortKey == 'clicks':
            if sortOrder.lower() == 'asc':
                objects.sort(key=lambda objects: objects.clicks)
            elif sortOrder.lower() == 'dec':
                objects.sort(key=lambda objects: objects.clicks, reverse=True)
            else:
                raise Exception("invalid sortkey")
        elif sortKey == 'views':
            if sortOrder.lower() == 'asc':
                objects.sort(key=lambda objects: objects.views)
            elif sortOrder.lower() == 'dec':
                objects.sort(key=lambda objects: objects.views, reverse=True)
            else:
                raise Exception("invalid sortkey")

        return objects
