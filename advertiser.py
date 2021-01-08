from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    @classmethod
    def help(self):
        return 'Id: id of this field is autoInc\nviews: nubmer of show of this ad\
            \nnumber: nubmer of click of this ad\nname: name of this ad'
    
    @staticmethod
    def getTotalClicks():
        return __class__.clicks

