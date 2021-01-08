from base_model import BaseAdvertising
from ad import Ad
from advertiser import Advertiser
 
if __name__ == "__main__":
    baseAdvertising = BaseAdvertising()
    advertiser1 = Advertiser('name1')
    advertiser2 = Advertiser('name2')
    ad1 = Ad("title1", "img-url1", "link1", advertiser1)
    ad2 = Ad("title2", "img-url2", "link2", advertiser2)
    baseAdvertising.describeMe()
    ad2.describeMe()
    advertiser1.describeMe()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()
    advertiser2.getName()
    advertiser2.setName("new name")
    advertiser2.getName()
    ad1.getClicks()
    advertiser2.getClicks()
    Advertiser.getTotalClicks()
    Advertiser.help()
    print(Advertiser.views)


    