from abc import ABC, abstractmethod
import datetime


class BaseAdvertising(ABC):
    id = -1
    def __init__(self):
        self.__class__.id += 1
        self.id = self.__class__.id
        self.views = 0
        self.clicks = 0
        self.creation_date = datetime.datetime.now()

    @abstractmethod
    def describeMe(self):
        raise NotImplementedError()

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1

    def incViews(self):
        self.views += 1


