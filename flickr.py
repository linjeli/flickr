import requests

def search(keyword):
    url = f'https://api.flickr.com/services/rest'
    data = {
        'sort': 'relevance',
        'parse_tags': 1,
        'content_type': 7,
        'per_page': 100,
        'page': 2,
        'lang': 'zh-HK',
        'text': keyword,
        'viewerNSID': '194826187@N03',
        'method': 'flickr.photos.search',
        'csrf': '1642517802:0iwbp9jhumhl:77df56e2d293a869789ba3b12238bdd2',
        'api_key': '37e307fcda728be12e35971622ee2bd6',
        'format': 'json',
        'hermes': 1,
        'hermesClient': 1,
        'reqId': '6dc87a11-5e71-4d5e-a6ba-e950a31f5e64',
        'nojsoncallback': 1,
    }
    resp = requests.get(url, headers=headers, params=data).json()
    items = resp.get('photos').get('photo')
    pic_url_list = []
    for item in items:
        owner = item.get('owner')
        id = item.get('id')
        pic_url = f'https://www.flickr.com/photos/{owner}/{id}/sizes/'
        pic_url_list.append(pic_url)
        print(pic_url)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'cookie': 'xb=120702; AMCVS_48E815355BFE96970A495CD0%40AdobeOrg=1; s_cc=true; _gcl_au=1.1.1295400934.1642476782; sp=062d127f-9e6c-4a11-8fa0-ca7aea6b7715; __ssid=cf5eb11b72dd8ae3a39e6f85f6ada2b; localization=zh-hk%3Bhk%3Bhk; ffs=194803133-8851; cookie_session=194803133%3A2873cb51a1067f1cb56974fae6322687; cookie_accid=194803133; cookie_epass=2873cb51a1067f1cb56974fae6322687; sa=1647661602%3A194826187%40N03%3Ab2820e6dae39ab5075ed5c4c966ae476; ccc=%7B%22needsConsent%22%3Afalse%2C%22managed%22%3A0%2C%22changed%22%3A0%2C%22info%22%3A%7B%22cookieBlock%22%3A%7B%22level%22%3A0%2C%22blockRan%22%3A0%7D%7D%2C%22freshServerContext%22%3Atrue%7D; __gads=ID=2b6307e487fd1da4:T=1642477607:S=ALNI_MaV2cxWlE_WxLGF7k5HDzk0ZzIurw; _sp_ses.df80=*; liqpw=1280; liqph=608; AMCV_48E815355BFE96970A495CD0%40AdobeOrg=281789898%7CMCMID%7C25370431293501094791378298294693824336%7CMCAAMLH-1643090828%7C11%7CMCAAMB-1643090828%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1642493228s%7CNONE%7CvVersion%7C4.1.0; s_sq=%5B%5BB%5D%5D; adCounter=6; cto_bundle=W--QZF9FcXV3VUJKSWgzbWZqYlFrVnIySEJUaXhMTUNFNDcxcDclMkZxajU0NjVJQUpFemNHUGpEZVcxSzhoNWZ2SGJUWVlndUN6NXNHRDh2Rms2elo5Vk1FcUFySmRRZU9DJTJCdTZhMTlHd3dLV1RRcUdnSUclMkJQOTk2WWRFUW9yclJpTTQlMkZqcDU5dWp5JTJGNGd5STB4VWY4N3ZYWHlnJTNEJTNE; cto_bidid=xLN4S19acEdPVEdYYVZUNjVMUTQlMkJ0S2F6alN4UlZkZEp3SmxXRWtBbWUxeUdsN0c1QjRlWnZOeSUyQnJXTVlodnFPNjMlMkIweVRiMHBSa0lLbUduJTJCOW1YcWR3elZEYTc3NXB5SDN1dzZZJTJCc0NvWDNtcFElM0Q; s_ptc=%5B%5BB%5D%5D; vp=346%2C642%2C2%2C15%2Csearch-photos-contacts-view%3A1012%2Csearch-photos-everyone-view%3A346; _sp_id.df80=e9965078-5c03-467b-9340-2427c720fba4.1642476781.2.1642489149.1642477637.b655a6de-fc28-444d-a335-20d734efb980; s_tp=1343; s_ppv=fluid-error-page-view%2C49%2C49%2C657; flrbp=1642489967-30a07d3a10573b8e6e686618e17c14ca533ae787; flrbgrp=1642489967-3ba0c18b0316f3c1835284e1be9ebe6d387c39bb; flrbgdrp=1642489967-1f3a1385a8a65d60419dfa4a2df4d43d32e45f4f; flrbgmrp=1642489967-028988c7457cebfc44565c928a8d1e476f6e22b2; flrbrst=1642489967-16c232c6f2517e7fc1e138aac3b1dddbc8d19c18; flrtags=1642489967-8e409abfe66228338358f72b23bbf7027a323d52; flrbfd=1642489967-4b1214220180d6651767d8712382b25511b7d152; flrbrp=1642489967-1fc9110734fe34f99674cdf01a5a6da927a9669c; flrb=28',
    }
    keyword = '风景'
    search(keyword)