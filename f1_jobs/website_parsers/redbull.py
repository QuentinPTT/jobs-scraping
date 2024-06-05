import requests

headers = {
    'Referer': 'https://www.redbullracing.com/',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

def get_jobs():
    response = requests.get('https://rbrworkday.redbull.com/', headers=headers)
    return parse_jobs(response.json()["Report_Entry"])

def parse_jobs(data):
    return data