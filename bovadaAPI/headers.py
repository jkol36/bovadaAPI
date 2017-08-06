import requests

cookies = {
    'JOINED': 'true',
    'BG_UA': 'Desktop|OS X|10_12_1|Chrome|55.0.2883.95||',
    'ux': 'created=true',
    'ln_grp': '2',
    'LANGUAGE': 'en',
    'ADRUM': 's=1483171346890&r=https%3A%2F%2Fwww.bovada.lv%2F%3F0',
    'has_js': '1',
    'DEFLANG': 'en',
    's_cc': 'true',
    'bsp': '1',
    's_fid': '25EB81C40CBC6670-086F7CF1DDF960B8',
    's_sq': 'bdbovadalv%3D%2526pid%253DbovadaLV%25253AHome%2526pidt%253D1%2526oid%253DLogin%2526oidt%253D3%2526ot%253DSUBMIT',
}

headers = {
    'Origin': 'https://www.bovada.lv',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.bovada.lv/?overlay=login',
    'Connection': 'keep-alive',
    'ADRUM': 'isAjax:true',
}

data = '{"username":"jonathankolman@gmail.com","password":"MakingMoney1995"}'

requests.post('https://www.bovada.lv/services/web/v2/oauth/token', headers=headers, cookies=cookies, data=data)


def get_bovada_headers_generic():
	return headers

def get_bovada_headers_authorization(auth_token, token_type):
	headers = get_bovada_headers_generic()
	headers["Authorization"] = token_type+" "+auth_token
	return headers


