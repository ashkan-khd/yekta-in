from base_model import BaseAdvertising
from ad import Ad
import time

class Advertiser(BaseAdvertising):
    advertisers = []
    def __init__(self, name):
        super().__init__()
        self.__class__.advertisers.append(self)
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def describeMe(self):
        return 'this class store ad info'

    @classmethod
    def help(cls):
        return 'Id: id of this field is autoInc\nviews: nubmer of show of this ad\
            \nnumber: nubmer of click of this ad\nname: name of this ad'

    @staticmethod
    def getTotalClicks():
        clickSum = 0
        for adver in Advertiser.advertisers:
            clickSum += adver.clicks
        return clickSum
    @staticmethod
    def sort_by_date():
        for adver in Advertiser.advertisers:
            print(adver.creation_date)
    

    @staticmethod
    def getObjectDataInJson():
        data =[]
        for adver in Advertiser.advertisers:
            data.append({"adver id":adver.id,"adver name":adver.name,"adver total clicks": adver.clicks, "adver total views": adver.views})
        
        return data
    
    @staticmethod
    def getObjectWithId(id):
        for advertiser in Advertiser.advertisers:
            if advertiser.id == id:
                return advertiser
                
        return None
        
    
        
