from ad import Ad
from advertiser import Advertiser


adver1 = Advertiser('ash')
adver2 = Advertiser('ali')
adver3 = Advertiser('mamad')

ad1 = Ad('spring', 'link', 'link', adver1)
ad2 = Ad('winter', 'link', 'link', adver1)
ad3 = Ad('winter', 'link', 'link', adver2)
ad1.incClicks()
ad1.incClicks()
ad1.incClicks()

ad2.incClicks()
ad2.incClicks()



print('Clicks: should be 3',ad1.clicks)
print('Clicks: should be 2',ad2.clicks)
print('Clicks: should be 0',ad3.clicks)


print('ash',adver1.clicks)
print('ali',adver2.clicks)



print('pop',Advertiser.getTotalClicks())

# ad  nm   co
# ad1 ash  3
# ad2 ash  2
# ash      5
# ad3 ali  0

