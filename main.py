from ad import Ad
from advertiser import Advertiser

if __name__ == "__main__":
    ashkan = Advertiser('ashkan')
    ali = Advertiser('ali')
    laptop = Ad('lap', 'lap', 'lap', ashkan)
    mobile = Ad('mobile', 'mobile', 'mobile', ali)
    dildo = Ad('dildo', 'dildo', 'dildo', ali)
    laptop.inc_views(); laptop.inc_views(); laptop.inc_views()
    laptop.inc_clicks()
    mobile.inc_views(); mobile.inc_views()
    mobile.inc_clicks(); mobile.inc_clicks()
    dildo.inc_views(); dildo.inc_views(); dildo.inc_views(); dildo.inc_views()
    dildo.inc_clicks(); dildo.inc_clicks(); dildo.inc_clicks()
    print(ashkan)
    print(ali)
    advertisers = Advertiser.sort_and_get_objects('dec')
    print([str(advertiser) for advertiser in advertisers])
    print(Advertiser.get_object_with_id(1))
    print(Ad.get_object_with_id(2))