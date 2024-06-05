import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',
    'origin': 'https://alcority.wd1.myworkdayjobs.com',
    'priority': 'u=1, i',
    'referer': 'https://alcority.wd1.myworkdayjobs.com/WilliamsRacing',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'x-calypso-csrf-token': '95e79a04-5534-4bde-b915-2d2a7e164f88',
}

json_data = {
    'appliedFacets': {},
    'limit': 20,
    'offset': 0,
    'searchText': '',
}

def get_jobs() -> list:
    '''
    Get jobs from the Williams Racing website.
    '''
    response = requests.post(
        'https://alcority.wd1.myworkdayjobs.com/wday/cxs/alcority/WilliamsRacing/jobs',
        headers=headers,
        json=json_data,
    )
    return parse_jobs(response.json()["jobPostings"])

def parse_jobs(data) -> list:
    return data