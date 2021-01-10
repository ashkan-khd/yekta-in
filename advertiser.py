from base_model import BaseAdvertising

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

    # @classmethod
    # def getTotalClicks(cls):
    #     clickSum = 0
    #     for adver in cls.advertisers:
    #         clickSum += adver.clicks
    #     return clickSum


