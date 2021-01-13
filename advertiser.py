from base_model import BaseAdvertising
from ad import Ad
import time

class Advertiser(BaseAdvertising):
    advertisers: list = []
    def __init__(self, name) -> None:
        super().__init__()
        self.__class__.advertisers.append(self)
        self.name: str = name

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name

    def describeMe(self) -> str:
        return 'this class store ad info'

    @classmethod
    def help(cls) -> str:
        return 'Id: id of this field is autoInc\nviews: nubmer of show of this ad\
            \nnumber: nubmer of click of this ad\nname: name of this ad'

    @staticmethod
    def getTotalClicks() -> int:
        clickSum = 0
        for adver in Advertiser.advertisers:
            clickSum += adver.clicks
        return clickSum

    @staticmethod
    def sort_by_date() -> list[object]:
        #TODO
        pass
    

    @staticmethod
    def getObjectDataInJson() -> list:
        data =[]
        for adver in Advertiser.advertisers:
            data.append({"adver id":adver.id,"adver name":adver.name,"adver total clicks": adver.clicks, "adver total views": adver.views})
        
        return data
    
    @staticmethod
    def getObjectWithId(id) -> object:
        for advertiser in Advertiser.advertisers:
            if advertiser.id == id:
                return advertiser
                
        return None
        
    
        
