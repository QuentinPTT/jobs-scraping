import requests

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'fr-FR,fr;q=0.7',
    'content-type': 'application/json',
    'lumesse-language': 'UK',
    'origin': 'https://cdn.group.renault.com',
    'password': 'guest',
    'priority': 'u=1, i',
    'referer': 'https://cdn.group.renault.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'username': 'PM1FK026203F3VBQB68V78M2I:guest:FO',
}

params = {
    'firstResult': '0',
    'maxResults': '100',
    'sortBy': '52',
    'sortOrder': 'desc',
}

json_data = {
    'searchCriteria': {
        'criteria': [
            {
                'key': 'Resultsperpage',
                'values': [
                    '100',
                ],
            },
        ],
    },
}

def get_jobs():
    response = requests.post(
        'https://emea5-foc.lumessetalentlink.com/fo/rest/jobs',
        params=params,
        headers=headers,
        json=json_data,
    )
    return parse_jobs(response.json()["jobs"])

def parse_jobs(data):
    return data