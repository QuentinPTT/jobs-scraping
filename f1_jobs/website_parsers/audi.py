import requests

headers = {
    'accept': '*/*',
    'accept-language': 'fr-FR,fr;q=0.7',
    # 'cookie': 'locale=en; internal_channel_id=1017414',
    'if-modified-since': 'Wed, 29 May 2024 16:15:55 GMT',
    'if-none-match': 'W/"88a3611516e1dee27f04c0af03fa1d19"',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
}

def get_jobs():
    response = requests.get('https://audi-formula-racing.jobs.personio.de/search.json', headers=headers)
    return parse_jobs(response.json())

def parse_jobs(data):
    return data